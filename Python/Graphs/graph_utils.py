from graph import Graph


def create_sample_graph() -> Graph:
    """Create a standard graph for algorithm testing"""
    g = Graph()

    # Build this graph:
    #   A --- B --- D
    #   |     |     |
    #   C     E --- F
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("D", "F")
    g.add_edge("E", "F")

    return g


def create_disconnected_graph() -> Graph:
    """Graph with two disconnected components"""
    g = Graph()

    # Component 1: A-B-C
    g.add_edge("A", "B")
    g.add_edge("B", "C")

    # Component 2: D-E-F
    g.add_edge("D", "E")
    g.add_edge("E", "F")

    return g
