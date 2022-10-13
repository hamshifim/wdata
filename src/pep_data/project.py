#!/usr/bin/env python
"""
Author: Gideon Bar
"""

from wielder.util.hocon_util import resolve_ordered


def get_project_conf():

    project_conf = '../conf/project.conf'

    ordered_project_files = [project_conf]

    injection = {
        "moto": "who dares, wins!"
    }

    conf = resolve_ordered(
        ordered_conf_paths=ordered_project_files,
        injection=injection
    )

    return conf
