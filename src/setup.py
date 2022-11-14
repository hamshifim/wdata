from setuptools import setup, find_packages

setup(name='pep_data',
      version='0.1',
      description='A repo for data exploration python sdk and notebooks',
      url='git@github.com:Pepticom/pep-data.git',
      author='gideonbar',
      author_email='gideon.bar@pepticom.com',
      license='Private',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['pyspark==3.0.1', 'pyspark-stubs==3.0.0.post3', 'matplotlib==3.6.1', 'matplotlib-inline==0.1.6', 'pandas==1.5.0','jupyter==1.0.0', 'treelib==1.6.1']
      )
