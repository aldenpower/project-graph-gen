import configparser
import matplotlib.pyplot as plt
import datetime as dt

class GetConfig():
    def __init__(self, configfile):
        self.config = configparser.ConfigParser()
        self.config_ = self.config.read(configfile)
        self.settings = self.config['settings']
        self.tittle = self.settings['tittle']
        self.style = self.settings['style']
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
    def __init__(self, style):
        self.st = plt.style.use(style)
        self.fig, self.ax = plt.subplots()
        # self.xticks = plt.xticks([])
        self.fonttittle = {'family':'sans','color':'black','size': 22, 'fontweight' : "bold"}
        self.font = {'family':'sans','color':'black','size':15}
        self.font2 = {'family':'sans','color':'black','size':15}
        self.bar_width = 0.2
        self.tittle_pad = 65
        self.xlabel_pad = 6.0
        self.xtext = -0.48
        self.label_location_x = 0.58
        self.label_location_y = -0.13
        self.label_ncols = 4
        self.annotate_rect_color = "darkslategray"
        # Planned config
        self.planned_line_color = "black"
        self.planned_annotate_offset = 3
        self.planned_line_marker = "s"
        # Accomplished config
        self.accomplished_line_color = "green"
        self.accomplished_annotate_offset = - 3
        self.accomplished_line_marker = "o"
        # Replanned config
        self.replanned_line_color = "red"
        self.replanned_line_marker = "s"
    def autolabel(self, rectangle_group):
        for rect in rectangle_group:
            height = rect.get_height()
    
            self.ax.annotate(str(height), xy = (rect.get_x() + rect.get_width() / 4, height),
            xytext = (-0.3, 1.0), textcoords = 'offset points',
            color = 'green')
    def annotate_line(self, line, offset):
        for x, y, n in zip(line[0], line[1], range(0, len(line[0]))):
            self.ax.annotate(line[1][n], (x, y + offset))

    def annotate_eff(self, x, value):
        for n, c in zip(range(0, len(x)), value):
            self.ax.annotate(c, (n - 0.4, 2), color = self.annotate_rect_color, fontweight = "bold")
    def annotate_planned(self, x, value):
        # Catch the min week num for axis value
        min_num = []
        for var in x:
            num = ""
            for c in var:
                if c.isdigit() and var:
                    num = num + c
                    min_num.append(int(num))
        
        minor = min(min_num)
        if minor == 0:
            for n, c in zip(range(0, len(x)), value):
                self.ax.annotate(c, (n + 0.16, 2), color = self.planned_line_color, fontweight = "bold")
        else:
            for n, c in zip(range(minor - 1, len(x) + minor), value):
                self.ax.annotate(c, (n + 0.16, 2), color = self.planned_line_color, fontweight = "bold")


    def annotate_accomplished(self, x, value):
        # Catch the min week num for axis value
        min_num = []
        for var in x:
            num = ""
            for c in var:
                if c.isdigit():
                    num = num + c
                    min_num.append(int(num)
                    )
        minor = min(min_num)
        if minor == 0:
            for n, c in zip(range(0, len(x)), value):
                self.ax.annotate(c, (n + 0.16, 6), color = self.accomplished_line_color, fontweight = "bold")
        else:
            for n, c in zip(range(minor - 1, len(x) + minor), value):
                self.ax.annotate(c, (n + 0.16, 6), color = self.accomplished_line_color, fontweight = "bold")

    
    def annotate_replanned(self, x, value):
        # Catch the min week num for axis value
        min_num = []
        for var in x:
            num = ""
            for c in var:
                if c.isdigit():
                    num = num + c
                    min_num.append(int(num))

        minor = min(min_num)
        if minor == 0:
            for n, c in zip(range(0, len(x) + minor), value):
                self.ax.annotate(c, (n + 0.16, 11), color = self.replanned_line_color, fontweight = "bold")
        else:
            for n, c in zip(range(minor - 1, len(x) + minor), value):
                self.ax.annotate(c, (n + 0.16, 11), color = self.replanned_line_color, fontweight = "bold")
