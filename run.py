from main import GetConfig, GraphConfig
import datetime as dt
import matplotlib.pyplot as plt

# Generate configuration object
configuration        = GetConfig('config.cfg')
graph_config         = GraphConfig(configuration.style)

if __name__ == '__main__':
    # Tittle configuration
    graph_config.ax.set_title(
    configuration.tittle,
    fontdict = graph_config.fonttittle,
    pad = graph_config.tittle_pad
    )

    # Settings text
    graph_config.ax.text(
    graph_config.xtext,
    max(configuration.accomplished_eff) + 15,
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
    marker = graph_config.planned_line_marker,
    color = graph_config.planned_line_color,
    label = 'planned'
    )
    graph_config.annotate_line_bottom(
    configuration.planned_values[0],
    configuration.planned_values[1],
    graph_config.annotate_planned_line_y,
    graph_config.planned_line_color
    )
    # Planned line values
    # graph_config.annotate_line(configuration.planned_values, graph_config.planned_annotate_offset)
    
    # Accomplished line
    accomplished_line = graph_config.ax.plot(
    configuration.accomplished_values[0],
    configuration.accomplished_values[1],
    marker = graph_config.accomplished_line_marker,
    color = graph_config.accomplished_line_color,
    label = 'accomplished'
    )
    
    graph_config.annotate_line_bottom(
    configuration.accomplished_values[0],
    configuration.accomplished_values[1],
    graph_config.annotate_accomplished_line_y,
    graph_config.accomplished_line_color
    )
    # graph_config.annotate_line(configuration.accomplished_values, graph_config.accomplished_annotate_offset)

    # Replanned line
    replanned_line = graph_config.ax.plot(
    configuration.replanned_values[0],
    configuration.replanned_values[1],
    marker = graph_config.replanned_line_marker,
    color = graph_config.replanned_line_color,
    label = 'replanned'
    )
    graph_config.annotate_line_bottom(
    configuration.replanned_values[0],
    configuration.replanned_values[1],
    graph_config.annotate_replanned_line_y,
    graph_config.replanned_line_color
    )

    # Rectangle
    rect1 = graph_config.ax.bar(
    configuration.accomplished_values[0],
    configuration.accomplished_eff_form,
    graph_config.bar_width,
    label = 'accomplished efficience',
    color = graph_config.annotate_rect_color)

    graph_config.autolabel(rect1)

    # Uncomment for annotate rect at bottom
    # graph_config.annotate_eff(
    # configuration.accomplished_eff,
    # configuration.accomplished_eff_form)


    # Label names
    graph_config.ax.set_xlabel(
    'Weeks',
    fontdict = graph_config.font,
    labelpad = graph_config.xlabel_pad)

    graph_config.ax.set_ylabel(
    'Percentage (%)',
    fontdict = graph_config.font2)

    # Label configuration
    plt.legend(
    loc = (graph_config.label_location_x,
           graph_config.label_location_y
          ),
           ncol = graph_config.label_ncols
    )

    # Show the graph
    plt.show()
