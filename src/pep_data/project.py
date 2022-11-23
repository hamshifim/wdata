#!/usr/bin/env python
"""
Author: Gideon Bar
"""

from wielder.util.hocon_util import resolve_ordered
from wielder.wield.project import get_super_project_roots, get_super_project_wield_conf


def project_conf():

    staging_root, super_project_root, project_name = get_super_project_roots()
    conf_path = f'{super_project_root}/wdata/conf'

    conf = get_super_project_wield_conf(
        project_conf_root=conf_path,
        call_from_jupyter=True
    )

    return conf


def quick_conf():

    staging_root, super_project_root, project_name = get_super_project_roots()
    project_conf = f'{super_project_root}/wdata/src/conf/project.conf'

    ordered_project_files = [project_conf]

    injection = {
        "moto": "Who dares, wins!",
        "staging_root": staging_root,
        "super_project_root": super_project_root,
        "project_name": project_name,
    }

    conf = resolve_ordered(
        ordered_conf_paths=ordered_project_files,
        injection=injection
    )

    return conf
