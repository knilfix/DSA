from typing import Dict
from collections import deque


class Graph:
    def __init__(self) -> None:
        self.graph: Dict[str, list[str]] = {}

    def add_vertex(self, vertex: str):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []

    def add_edge(self, src: str, dest: str, directed=False):
        self.add_vertex(src)
        self.add_vertex(dest)

        if dest not in self.graph[src]:
            self.graph[src].append(dest)

        if not directed and src not in self.graph[dest]:
            self.graph[dest].append(src)

    def get_neighbors(self, vertex: str) -> list[str]:

        if vertex not in self.graph.keys():
            return []

        return self.graph[vertex]

    def get_vertices(self) -> list[str]:
        return list(self.graph.keys())

    def has_vertex(self, vertex: str) -> bool:
        if vertex in self.graph.keys():
            return True
        return False

    def has_edge(self, src: str, dest: str) -> bool:
        """
        Check if edge exists between two vertices.

        Input:
            src: str - source vertex
            dest: str - destination vertex
        Output:
            bool - True if edge exists, False otherwise
        """

        if src not in self.graph.keys() or dest not in self.graph.keys():
            return False

        if dest in self.graph[src]:
            return True

        return False

    def remove_vertex(self, vertex: str) -> bool:
        """
        Remove vertex and all its edges from graph.

        Input:
            vertex: str - vertex to remove
        Output:
            bool - True if removed, False if vertex didn't exist
        """
        if vertex not in self.graph.keys():
            return False

        self.graph.pop(vertex)
        return True

    def remove_edge(self, src: str, dest: str, directed: bool = False) -> bool:
        """
        Remove edge between two vertices.

        Input:
            src: str - source vertex
            dest: str - destination vertex
            directed: bool - if True, only remove src→dest
        Output:
            bool - True if edge existed and was removed
        """
        if src in self.graph.keys() and dest in self.graph.keys():
            self.graph[src].remove(dest)

            if not directed:
                self.graph[dest].remove(src)

            return True
        else:
            return False

    def print_graph(self):
        """Print the graph in a clean, readable format"""
        print("\n" + "=" * 40)
        print("GRAPH ADJACENCY LIST")
        print("=" * 40)

        if not self.graph:
            print("Graph is empty!")
            return

        for vertex in sorted(self.graph.keys()):
            neighbors = self.graph[vertex]
            if neighbors:
                print(f"Vertex '{vertex}': {neighbors}")
            else:
                print(f"Vertex '{vertex}': [] (no connections)")
        print("=" * 40)


def main():
    """Comprehensive test of all Graph methods"""

    g = Graph()

    print("🧪 COMPREHENSIVE GRAPH TESTING")
    print("=" * 60)

    # Test 1: Empty graph operations
    print("\n1. Testing empty graph:")
    print(f"Vertices: {g.get_vertices()}")
    print(f"Has vertex 'A': {g.has_vertex('A')}")
    print(f"Has edge A→B: {g.has_edge('A', 'B')}")
    g.print_graph()

    # Test 2: Vertex operations
    print("\n2. Testing vertex operations:")
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")  # Isolated vertex
    print(f"Vertices: {g.get_vertices()}")
    print(f"Has vertex 'A': {g.has_vertex('A')}")
    print(f"Has vertex 'X': {g.has_vertex('X')}")
    g.print_graph()

    # Test 3: Undirected edges
    print("\n3. Testing undirected edges:")
    g.add_edge("A", "B")  # A ↔ B
    g.add_edge("B", "C")  # B ↔ C
    g.add_edge("A", "D")  # A ↔ D
    print(f"Has edge A→B: {g.has_edge('A', 'B')}")
    print(f"Has edge B→A: {g.has_edge('B', 'A')}")  # Should be True (undirected)
    print(f"Has edge A→C: {g.has_edge('A', 'C')}")  # Should be False
    g.print_graph()

    # Test 4: Directed edges
    print("\n4. Testing directed edges:")
    g.add_edge("C", "D", directed=True)  # Only C → D
    print(f"Has edge C→D: {g.has_edge('C', 'D')}")  # Should be True
    print(f"Has edge D→C: {g.has_edge('D', 'C')}")  # Should be False (directed)
    g.print_graph()

    # Test 5: Neighbor retrieval
    print("\n5. Testing neighbor retrieval:")
    print(f"Neighbors of A: {g.get_neighbors('A')}")
    print(f"Neighbors of B: {g.get_neighbors('B')}")
    print(f"Neighbors of C: {g.get_neighbors('C')}")
    print(f"Neighbors of D: {g.get_neighbors('D')}")
    print(f"Neighbors of E: {g.get_neighbors('E')}")  # Isolated vertex
    print(f"Neighbors of X: {g.get_neighbors('X')}")  # Non-existent

    # Test 6: Duplicate prevention
    print("\n6. Testing duplicate prevention:")
    g.add_edge("A", "B")  # Should not create duplicates
    g.add_vertex("A")  # Should not reset neighbors
    print(f"Neighbors of A (after duplicates): {g.get_neighbors('A')}")
    g.print_graph()

    # Test 7: Remove operations
    print("\n7. Testing remove operations:")
    print(f"Remove edge A→B: {g.remove_edge('A', 'B')}")  # Remove A ↔ B connection
    print(f"Has edge A→B after removal: {g.has_edge('A', 'B')}")
    print(f"Has edge B→A after removal: {g.has_edge('B', 'A')}")
    g.print_graph()

    # Test 8: Remove vertex
    print("\n8. Testing vertex removal:")
    print(f"Remove vertex E: {g.remove_vertex('E')}")  # Isolated vertex
    print(f"Remove vertex X: {g.remove_vertex('X')}")  # Non-existent
    print(f"Vertices after removal: {g.get_vertices()}")
    g.print_graph()

    # Test 9: BFS to demonstrate practical use
    print("\n9. Testing BFS traversal:")

    def bfs(graph, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in graph.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    print(f"BFS starting from A: {bfs(g, 'A')}")
    print(f"BFS starting from C: {bfs(g, 'C')}")


if __name__ == "__main__":
    main()
