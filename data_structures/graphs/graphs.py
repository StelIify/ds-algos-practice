from data_structures.queue import Queue


class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def __repr__(self):
        return self.value

    # for undirected graph, add mutual connection
    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)

    def add_adjacent_vertex_direct(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)


def dfs_search(vertex, value, seen_vertex=None):
    if vertex.value == value:
        return Vertex
    if not seen_vertex:
        seen_vertex = set()
    seen_vertex.add(vertex)
    print(f"path: {vertex}")
    for v in vertex.adjacent_vertices:
        if v.value == value:
            return v
        if v in seen_vertex:
            continue
        vertex_search = dfs_search(v, value, seen_vertex)
        if vertex_search:
            return vertex_search
    return None


def bfs_search(vertex, value):
    q = Queue(vertex)
    seen_vertex = {vertex.value: True}
    while len(q):
        current = q.dequeue()
        if current.value == value:
            return current
        print(f"path: {current}")
        for v in current.adjacent_vertices:
            if seen_vertex.get(v.value):
                continue
            elif v.value == value:
                return v
            else:
                seen_vertex[v.value] = True
                q.enqueue(v)
    return None


alice = Vertex("Alice")
bob = Vertex("Bob")
candy = Vertex("Candy")
derek = Vertex("Derek")
elaine = Vertex("Elaine")
fred = Vertex("Fred")
helen = Vertex("Helen")
gina = Vertex("Gina")
irena = Vertex("Irena")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)

bob.add_adjacent_vertex(fred)
fred.add_adjacent_vertex(helen)
helen.add_adjacent_vertex(candy)
derek.add_adjacent_vertex(elaine)
derek.add_adjacent_vertex(gina)
gina.add_adjacent_vertex(irena)

# dfs_traverse(alice)
# print()
print(bfs_search(alice, "Gina"))
print()
print(dfs_search(alice, "Gina"))
