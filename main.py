import configparser

class GraphGen():
    def __init__(self, configfile):
        self.config = configparser.ConfigParser()
        self.config_ = self.config.read(configfile)
        self.planned = self.config['planned']
        self.accomplished = self.config['accomplished']
        self.replanned = self.config['replanned']
    def get_sections(self, show = True):
        if show:
            secs = self.config.sections()
            print(secs)
            return secs
        return secs
    def get_planned(self, show = True):
        if show:
            print(self.planned)
            return self.planned
        return self.planned
    def get_accomplished(self, show = True):
        if show:
            print(self.accomplished)
            return self.accomplished
        return self.accomplished
    def get_values(self, section, show = True):
        pass
        
