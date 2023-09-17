#!/usr/bin/env python
# coding: utf-8
import os
"""
setting parameters needed to run the module
"""

class set_param:

    def __init__(self, site, conf_prefix, yearFrom, yearTo, interval, toShow):
        self.site = site
        self.conf_prefix = conf_prefix
        self.yearFrom = yearFrom
        self.yearTo = yearTo+1
        self.toShow = toShow
        self.interval = interval
        self.cachedir = './cache_gscholar' + '/' + conf_prefix
        if not os.path.isdir(self.cachedir):
            os.mkdir(self.cachedir)
