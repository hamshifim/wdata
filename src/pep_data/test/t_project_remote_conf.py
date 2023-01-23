#!/usr/bin/env python
from pep_data.project import data_project_conf
from wielder.wield.remote import get_remote_unique_context

if __name__ == "__main__":

    conf = data_project_conf()

    cont = get_remote_unique_context(conf)

    print(cont)
