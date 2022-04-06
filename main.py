import configparser

class GetConfig():
    def __init__(self, configfile):
        self.config = configparser.ConfigParser()
        self.config_ = self.config.read(configfile)
        self.settings = self.config['settings']
        self.planned = self.config['planned']
        self.accomplished = self.config['accomplished']
        self.replanned = self.config['replanned']
    def get_sections(self, show = True):
        if show:
            secs = self.config.sections()
            print(secs)
            return secs
        return secs
    def get_values(self, section):
        keys, values = [], []
        for key in section:
            keys.append(key) 
        for value in range(0, len(keys)):
            var = section[keys[value]]
            values.append(float(var))

        return keys, values

