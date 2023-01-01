#!/usr/bin/env python

import logging
from time import sleep

from pep_data.project import data_project_conf
from wielder.util.log_util import setup_logging
from wielder.util.sparker import get_sparker, SparkRuntime

if __name__ == "__main__":

    setup_logging(log_level=logging.DEBUG)
    conf = data_project_conf()

    if conf.runtime_env == 'aws':
        spark_runtime_env = SparkRuntime.EMR
    else:
        spark_runtime_env = SparkRuntime.DEV_SERVER

    sparker = get_sparker(conf, spark_runtime_env=spark_runtime_env)
    sparker.launch_jobs(jobs_path=['raw_models_to_csv'])

    while sparker.is_job_active(jobs_path=['raw_models_to_csv']):

        interval = 20
        logging.info(f'Sleeping {interval} to see if steps completed.')
        sleep(interval)

