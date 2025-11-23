from collections import deque
from graph import Graph


def bfs(graph: Graph, start: str) -> list[str]:
    visited = set()
    queue = deque(start)
    result = []

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            result.append(current)

            for neighbor in graph.get_neighbors(current):
                if neighbor not in visited:
                    queue.append(neighbor)

    return result
