#!/usr/bin/env python

import logging
from time import sleep

from pep_data.project import data_project_conf
from wielder.util.log_util import setup_logging
from wielder.util.sparker import get_sparker, SparkRuntime
from wielder.wield.remote import configure_remote_unique_context

if __name__ == "__main__":

    setup_logging(log_level=logging.DEBUG)
    conf = data_project_conf()

    configure_remote_unique_context(conf)

    if conf.runtime_env == 'aws':
        spark_runtime_env = SparkRuntime.EMR
    else:
        spark_runtime_env = SparkRuntime.DEV_SERVER

    sparker = get_sparker(conf, spark_runtime_env=spark_runtime_env)
    sparker.launch_jobs(jobs_path=['humanize_0'])

    while sparker.is_job_active(jobs_path=['humanize_0']):

        interval = 20
        logging.info(f'Sleeping {interval} to see if steps completed.')
        sleep(interval)

    sparker.launch_jobs(jobs_path=['humanize_1'])

    while sparker.is_job_active(jobs_path=['humanize_1']):

        interval = 20
        logging.info(f'Sleeping {interval} to see if steps completed.')
        sleep(interval)

    sparker.launch_jobs(jobs_path=['humanize_2'])
