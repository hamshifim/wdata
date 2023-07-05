#!/usr/bin/env python
from pep_data.project import data_project_conf

if __name__ == "__main__":

    conf = data_project_conf(app='milky_way')

    s = conf.milky_way.vantage_points.earth

    print(conf)

    print(s)
