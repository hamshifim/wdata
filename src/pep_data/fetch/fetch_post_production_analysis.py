#!/usr/bin/env python

import logging

from pep_data.fetch.data_fetcher import fetch_post_production_analysis

from pep_data.project import data_project_conf
from wielder.util.log_util import setup_logging

if __name__ == "__main__":
    setup_logging(log_level=logging.DEBUG)
    conf = data_project_conf()

    fetch_post_production_analysis(conf)
