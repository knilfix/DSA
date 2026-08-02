from dfs import dfs
from bfs import bfs
from graph_utils import create_sample_graph


def compare_traversals():
    g = create_sample_graph()

    print("===Traversals Comparison===")
    print(f"Graph: {g.print_graph()}")
    print(f"DFS from A: {dfs(g,'A')}")
    print(f"BFS from A: {bfs(g,'A')}")


if __name__ == "__main__":
    compare_traversals()
