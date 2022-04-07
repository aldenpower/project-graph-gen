import configparser
import matplotlib.pyplot as plt
import datetime as dt

class GetConfig():
    def __init__(self, configfile):
        self.config = configparser.ConfigParser()
        self.config_ = self.config.read(configfile)
        self.settings = self.config['settings']
        self.tittle = self.settings['tittle']
        self.start = dt.date.fromisoformat(self.settings['start'])
        self.end = dt.date.fromisoformat(self.settings['end'])
        self.planned = self.config['planned']
        self.accomplished = self.config['accomplished']
        self.replanned = self.config['replanned']
        self.settings_values = self.get_values(self.settings)
        self.planned_values = self.get_values(self.planned)
        self.accomplished_values = self.get_values(self.accomplished)
        self.replanned_values = self.get_values(self.replanned)
        self.accomplished_eff = self.get_eff(self.accomplished_values[1], self.planned_values[1])
        self.accomplished_eff_form = self.get_eff(self.accomplished_values[1], self.planned_values[1], format = True)
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
            if var.isdigit():
                values.append(float(var))
            else:
                values.append(var)
        return keys, values

    def get_eff(self, value1, value2, format = False):
        if format:
            eff = [a / b * 100 for a, b in zip(value1, value2)]
            eff_rounded = [float(f'{a:.2f}') for a in eff]
            return eff_rounded

        eff = [a / b * 100 for a, b in zip(value1, value2)]
        return eff 

class GraphConfig():
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.fonttittle = {'family':'sans','color':'black','size': 22, 'fontweight' : "bold"}
        self.font = {'family':'sans','color':'black','size':15}
        self.font2 = {'family':'sans','color':'black','size':15}
        self.bar_width = 0.2
        self.tittle_pad = 65
        self.xlabel_pad = 15.0
    def autolabel(self, rectangle_group):
        for rect in rectangle_group:
            height = rect.get_height()
    
            self.ax.annotate(str(height), xy = (rect.get_x() + rect.get_width() / 4, height),
            xytext = (20, -10), textcoords = 'offset points',
            color = 'grey')
    