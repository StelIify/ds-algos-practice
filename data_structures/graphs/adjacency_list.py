from typing import Dict, List
from collections import defaultdict, deque
from data_structures.queue import Queue


def bfs_traverse(graph: Dict, start):
    queue = Queue(start)

    while len(queue):
        current = queue.dequeue()
        print(current)
        for node in graph[current]:
            queue.enqueue(node)


def dfs_traverse(graph: Dict, start):
    stack = [start]

    while len(stack):
        current = stack.pop()
        print(current)
        for node in graph[current]:
            stack.append(node)


def dfs_traverse_rec(graph: Dict, start):
    current = start

    print(current)
    for node in graph[current]:
        dfs_traverse_rec(graph, node)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


# bfs_traverse(graph, "a")
# print()
# dfs_traverse_rec(graph, "a")


def detect_cycle_in_directed_graph(graph, source, seen=None):
    if not seen:
        seen = set()
    if source in seen:
        return True
    seen.add(source)
    for node in graph[source]:
        if detect_cycle_in_directed_graph(graph, node, seen):
            return True
    return False


graph_with_cycle = {
    1: [2],
    2: [3],
    3: [1, 4],
    4: [5],
    5: [6],
    6: [4]
}
graph_with_cycle2 = {
    "a": ["b"],
    "b": ["c"],
    "c": ["d"],
    "d": []
}


# print(detect_cycle_in_directed_graph(graph_with_cycle2, "a"))


def has_path(graph, source, dest):
    queue = Queue(source)

    while queue:
        current = queue.dequeue()
        if current == dest:
            return True
        for neighbour in graph[current]:
            queue.enqueue(neighbour)
    return False


path = {
    "f": ["i", "g"],
    "i": ["k", "g"],
    "g": ["h"],
    "k": [],
    "j": [],
    "h": []
}


# print(has_path(path, "j", "f"))


def connected_nodes_count(graph):
    seen = set()
    count = 0
    for node in graph.keys():
        if explore(graph, node, seen):
            count += 1
    return count


def explore(graph, current, seen):
    if current in seen:
        return False
    seen.add(current)
    for neighbour in graph[current]:
        explore(graph, neighbour, seen)
    return True


def connected_nodes_count_bfs(graph):
    seen = set()
    count = 0
    queue = Queue()
    for node in graph.keys():
        if node in seen:
            continue
        queue.enqueue(node)
        while queue:
            current = queue.dequeue()
            seen.add(current)
            for neighbour in graph[current]:
                if neighbour in seen:
                    continue
                queue.enqueue(neighbour)
        count += 1
        queue.clear()
    return count


test_graph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}


def create_adjacency_list(edges):
    adjacency_list = defaultdict(list)
    for start_node, end_node in edges:
        adjacency_list[start_node].append(end_node)
        # for undirected graph
        adjacency_list[end_node].append(start_node)
    return adjacency_list


# print(connected_nodes_count(test_graph))  # 3
# print(connected_nodes_count_bfs(test_graph))


# edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
# print(create_adjacency_list(edges))
def count_islands(grid):
    seen = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore_grid(grid, r, c, seen):
                count += 1
    return count


def explore_grid(grid, r, c, seen):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])
    if not row_inbound or not col_inbound:
        return False
    if grid[r][c] == "W":
        return False
    if (r, c) in seen:
        return False
    seen.add((r, c))

    explore_grid(grid, r - 1, c, seen)  # up
    explore_grid(grid, r + 1, c, seen)  # down
    explore_grid(grid, r, c - 1, seen)  # left
    explore_grid(grid, r, c + 1, seen)  # right

    return True


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]


# print(count_islands(grid))  # 3


def numIslands(grid: List[List[str]]) -> int:
    count = 0
    seen = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore2(grid, r, c, seen):
                count += 1
    return count


def explore2(grid, r: int, c: int, seen):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])

    if not row_inbound or col_inbound:
        return False
    if grid[r][c] == "0":
        return False
    if (r, c) in seen:
        return False
    seen.add((r, c))

    explore2(grid, r - 1, c, seen)  # top
    explore2(grid, r + 1, c, seen)  # bottom
    explore2(grid, r, c - 1, seen)  # left
    explore2(grid, r, c + 1, seen)  # righ

    return True


g = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(numIslands(g))
