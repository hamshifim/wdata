#!/usr/bin/env python

import logging
import os

from pep_data.project import data_project_conf
from wielder.util.bucketeer import AWSBucketeer
from wielder.util.log_util import setup_logging
from wielder.wield.project import get_local_path

if __name__ == "__main__":

    setup_logging(log_level=logging.DEBUG)
    conf = data_project_conf()

    b = AWSBucketeer(conf)

    experiment_path = conf.unique_config_path
    experiment_path = f'{experiment_path}/BOT_DISPATCH/LOGS/HOT_PEPTIDES'

    bucket_name = conf.namespace_bucket

    local_path = get_local_path(conf, experiment_path)

    os.system(f'atom {local_path}')

    b.download_objects_by_key(
        bucket_name=bucket_name,
        root_key=experiment_path,
        dest=local_path
    )




