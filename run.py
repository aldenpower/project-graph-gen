from main import GraphGen


if __name__ == '__main__':
    graph = GraphGen('config.cfg')

    sections = graph.get_sections()

    planned_section = graph.planned
    accomplished_section = graph.accomplished
