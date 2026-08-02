from graph import Graph


def dfs(graph: Graph, start: str) -> list[str]:

    visited = set()
    stack = [start]
    result = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            result.append(current)
            for neighbor in reversed(graph.get_neighbors(current)):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result
