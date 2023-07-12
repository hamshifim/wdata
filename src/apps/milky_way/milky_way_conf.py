#!/usr/bin/env python
from pep_data.project import data_project_conf

from wielder.util.hocon_util import merge_configurations
from wielder.wield.project import configure_project_module
from wielder.wield.remote import get_remote_unique_context

if __name__ == "__main__":
    conf = data_project_conf(app='milky_way')
    remote_conf = get_remote_unique_context(conf)

    merge_conf = merge_configurations(conf, remote_conf)

    configure_project_module(conf=merge_conf, module='unreal_data_visualization', app='milky_way')

