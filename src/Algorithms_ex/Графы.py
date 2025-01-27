from collections import deque

# Алгоритм поиска в глубину на Python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {
    "0": set(["1", "2"]),
    "1": set(["0", "3", "4"]),
    "2": set(["0"]),
    "3": set(["1"]),
    "4": set(["2", "3"]),
}




# Алгоритм поиска в ширину на Python

def bfs(graph, start_node):
    # Инициализация пустого множества для посещенных узлов
    visited = set()
    # Инициализация пустой очереди для обхода
    queue = deque()
    
    visited.add(start_node)
    queue.append(start_node)

    while queue:
        m = queue.popleft()
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return visited

dfs(graph, "0")