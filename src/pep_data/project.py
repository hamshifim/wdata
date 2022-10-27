#!/usr/bin/env python
"""
Author: Gideon Bar
"""

from wielder.util.hocon_util import resolve_ordered
from wielder.wield.project import get_super_project_root


def get_project_conf():

    _, project_root, _ = get_super_project_root()
    project_conf = f'{project_root}/pep-data/src/conf/project.conf'

    ordered_project_files = [project_conf]

    injection = {
        "moto": "who dares, wins!"
    }

    conf = resolve_ordered(
        ordered_conf_paths=ordered_project_files,
        injection=injection
    )

    return conf
