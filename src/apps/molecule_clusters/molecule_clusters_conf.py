#!/usr/bin/env python
from pep_data.project import data_project_conf

if __name__ == "__main__":

    conf = data_project_conf(app='molecule_clusters')

    s = conf.molecule_clusters.vantage_points.overview

    print(conf)

    print(s)
