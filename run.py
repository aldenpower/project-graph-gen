from main import GraphGen


if __name__ == '__main__':
    graph = GraphGen('config.cfg')

    graph.get_sections()

    graph.get_planned()
    graph.get_accomplished()
