#!/usr/bin/env python
import logging

from pep_data.project import data_project_conf
from wielder.util.log_util import setup_logging
from wielder.wield.project import default_conf_root, configure_project_module

if __name__ == "__main__":

    setup_logging(log_level=logging.DEBUG)

    project_conf_dir = default_conf_root()
    app = 'milky_way'
    conf = data_project_conf(app=app)

    configure_project_module(conf, app)


