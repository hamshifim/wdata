#!/usr/bin/env python
"""
Author: Gideon Bar
"""

from wielder.util.arguer import get_wielder_parser
from wielder.util.hocon_util import resolve_ordered
from wielder.wield.project import get_super_project_roots, get_super_project_wield_conf


def data_project_conf():
    staging_root, super_project_root, project_name = get_super_project_roots()
    conf_path = f'{super_project_root}/wdata/conf'
    wield_parser = get_wielder_parser()
    wield_parser.add_argument("-f", "--fff", help="a dummy argument to fool ipython", default="1")

    conf = get_super_project_wield_conf(
        project_conf_root=conf_path,
        wield_parser=wield_parser,
        # TODO make use Module configuration without breaking
        # configure_wield_modules=False,
        app='data'
    )

    return conf


def quick_conf():
    staging_root, super_project_root, project_name = get_super_project_roots()

    # here is a problem with the path on Windows
    project_conf = f'{super_project_root}/wdata/src/conf/project.conf'

    # a way to fix it so it works on all operating systems:
    # print(f'project_conf: {project_conf}')
    # # project_conf = os.path.join(super_project_root, 'wdata', 'src', 'conf', 'project.conf')
    # path_string = 'wdata/src/conf/project.conf'
    # project_conf = os.path.join(super_project_root, get_os_path(path_string))
    # print(f'project_conf: {project_conf}')

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


if __name__ == "__main__":
    quick_conf()
