from pyspark.sql.types import StructField, DoubleType, IntegerType, StringType, FloatType, BooleanType, StructType


def field_to_struct(header, floats=[], doubles=[], integers=[], booleans=[]):

    field_type = StringType()

    match header:
        case a if a in floats:
            field_type = FloatType()
        case a if a in integers:
            field_type = IntegerType()
        case a if a in doubles:
            field_type = DoubleType()
        case a if a in booleans:
            field_type = BooleanType()

    return StructField(header, field_type)


def base_df(spark, conf, app):

    app_conf = conf[app]

    cols_name = app_conf['cols_name']
    cols_double = app_conf['cols_double']
    cols_integer = app_conf['cols_integer']

    fields = [field_to_struct(header, doubles=cols_double, integers=cols_integer) for header in cols_name]
    schema = StructType(fields)

    data_path = app_conf['data_path']
    df = spark.read.schema(schema).csv(data_path)

    cols_to_keep = [x for x in df.columns if 'remove' not in x]
    df = df.select(*cols_to_keep)

    return df
