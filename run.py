from main import GetConfig, GraphConfig
import datetime as dt
import matplotlib.pyplot as plt

# Generate configuration object
configuration        = GetConfig('config.cfg')
graph_config         = GraphConfig()

if __name__ == '__main__':
    # Tittle configuration
    graph_config.ax.set_title(
    configuration.tittle,
    fontdict = graph_config.fonttittle,
    pad = graph_config.tittle_pad
    )

    # Settings text
    graph_config.ax.text(
    -0.25,
    max(configuration.accomplished_eff) + 25,
    'Project start date : {}\nProject end date: {}\nToday : {}\nElapsed time: {} days'.
    format(
        configuration.start,
        configuration.end,
        dt.date.today(),
        (dt.date.today() - configuration.start).days
        ),
    style='italic'
    )

    # Planned line
    planned_line = graph_config.ax.plot(
    configuration.planned_values[0],
    configuration.planned_values[1],
    marker = 'D',
    color = 'green',
    label = 'planned'
    )
    
    # Accomplished line
    accomplished_line = graph_config.ax.plot(
    configuration.accomplished_values[0],
    configuration.accomplished_values[1],
    marker = 'h',
    color = 'blue',
    label = 'accomplished'
    )
    
    # Replanned line
    replanned_line = graph_config.ax.plot(
    configuration.replanned_values[0],
    configuration.replanned_values[1],
    marker = 's',
    color = 'red',
    label = 'replanned'
    )

    # Positioning efficience bars
    x_accomplished = [x for x in range(len(configuration.accomplished_eff))]

    # Rectangle
    rect1 = graph_config.ax.bar(
    x_accomplished,
    configuration.accomplished_eff_form,
    graph_config.bar_width,
    label = 'accomplished efficience',
    color = 'darkslategray')
    graph_config.autolabel(rect1)


    # Label names
    graph_config.ax.set_xlabel(
    'Weeks',
    fontdict = graph_config.font,
    labelpad = graph_config.xlabel_pad)

    graph_config.ax.set_ylabel(
    'Percentage (%)',
    fontdict = graph_config.font2)

    # Show the plot
    plt.legend()
    plt.show()
