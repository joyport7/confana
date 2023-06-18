class set_param:

    def __init__(self, site, conf_prefix, yearFrom, yearTo, interval, toShow):
        self.site = site
        self.conf_prefix = conf_prefix
        self.yearFrom = yearFrom
        self.yearTo = yearTo+1
        self.toShow = toShow
        self.interval = interval
