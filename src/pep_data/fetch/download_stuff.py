#!/usr/bin/env python

import logging

from pep_data.project import data_project_conf
from wielder.util.log_util import setup_logging
from wielder.wield.remote import download_stuff

if __name__ == "__main__":

    setup_logging(log_level=logging.DEBUG)
    conf = data_project_conf()

    download_stuff(conf)




