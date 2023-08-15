#!/usr/bin/env python
# coding: utf-8

# Stars app
# =
# 
# An example app for ingesting spatial data into a format readable by the Unreal Engine application at git@github.com:hamshifim/unreal-data-visualization.git. Both this repository and the repository holding the Unreal are submodules of this super repo: git@github.com:hamshifim/data-wielder.git and it holds the compatible versions of both repositories. Make sure you checkout the commit pointed to by data-wielder submodules for version alignment.
# 
# If it's your first time run the notebook cell by cell to while looking at the output directories; I would recommend using Sublime Text to view the directories intended for generated files.
# 
# For we are using CSV to import larger datasets to Unreal and are not aware of usage of a format including schema (e.g. parquet) supported by unreal. The last cell in this notebook generates the structs for the Unreal Engine application. After you are done you should build the code in Unreal and run the application using the instructions in the Unreal submodule.

# In[ ]:


from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyhocon import ConfigFactory as CF
from pyhocon import HOCONConverter

from pep_data.project import data_project_conf
from wielder.spark.util import set_spark_env
from wielder.wield.project import default_conf_root, configure_project_module
from wielder.spark.util import to_unreal, columns_ranges
from wielder.spark.spatial import estimate_df_boundaries
from wielder.spark.util import color_by_range
from wielder.unreal.struct_gen import *


# In[ ]:


project_conf_dir = default_conf_root()
app = 'stars'
conf = data_project_conf(app=app)
configure_project_module(conf, app)

app_conf = conf[app]


# In[ ]:


unreal_conf = app_conf.unreal_conf
dest = unreal_conf.conf


# In[ ]:


set_spark_env()
spark = SparkSession.builder.config("spark.driver.memory", "15g").appName(app).getOrCreate()


# In[ ]:


src = app_conf.src.stars_raw
dff = spark.read.csv(src, header=True)


# In[ ]:


dff.show(5)


# In[ ]:


def random_rgb():
    import random
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())

random_rgb_udf = F.udf(random_rgb)


# In[ ]:


def random_normalized_num():
    import random
    return random.uniform(0.01, 0.1)

random_normalized_num_udf = F.udf(random_normalized_num)


# In[ ]:


# cols = ['Index'] + app_conf.unreal_conf.base_columns
df = dff \
    .withColumn("x", F.col("x").cast("float")) \
    .withColumn("y", F.col("y").cast("float")) \
    .withColumn("z", F.col("z").cast("float")) \
    .withColumn("type", F.lit('stars')) \
    .withColumn("color", random_rgb_udf()) \
    .withColumn("size", random_normalized_num_udf()) \
    .withColumn("opacity", random_normalized_num_udf())


# In[ ]:


df.show(5)


# In[ ]:


# df.printSchema()


# In[ ]:


main_table = 'stars'
table = 'metadata'


# In[ ]:


unreal_conf.data_types[main_table].data_source


# In[ ]:


dest = unreal_conf.data_types[main_table].data_source
to_unreal(df=df, dest=dest)


# In[ ]:


boundaries = estimate_df_boundaries(df)
boundaries


# In[ ]:


unreal_conf.views.galaxy['boundaries'] = CF.from_dict(boundaries)


# In[ ]:


src = app_conf.src.stars_parameters
_col = "p_life"
params_df = spark.read.csv(src, header=True) \
    .withColumn('likelihood_of_life', F.col('likelihood_of_life').cast('float')) \
    .withColumn(_col, F.floor(F.col("likelihood_of_life")))


# In[ ]:


params_df.show(5)


# In[ ]:


# params_df.printSchema()
# params_df.columns


# In[ ]:


dest1 = unreal_conf.data_types[main_table].tables[table]['data_source']
dest1


# In[ ]:


unreal_conf = to_unreal(params_df, dest1, unreal_conf, main_table, table, default_table=True)


# In[ ]:


# unreal_conf


# In[ ]:


ranges = columns_ranges(params_df, [_col])
_min = ranges[f'min_{_col}']
_max = ranges[f'max_{_col}']

color_codes = color_by_range(_min, _max, cold=True)

unreal_conf.views.galaxy.color_maps[_col] = CF.from_dict(color_codes)
color_codes


# In[ ]:


unreal_conf_j = HOCONConverter.to_json(unreal_conf, indent=4)
dest_j = unreal_conf.conf

with open(dest_j, 'w') as file:
    file.write(unreal_conf_j)


# In[ ]:


uconf = conf.unreal
solution_name = uconf.solution_name

if uconf.del_structs:
    delete_old_structs(solution_name, uconf.project_path)

# Define the path to your config file, written to location above
conf_path = uconf.conf_path
output_dir = uconf.struct_path

generate_structs(conf_path, output_dir)

