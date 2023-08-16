from data_structures.queue import Queue


class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def __repr__(self):
        return self.value

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)


def dfs_traverse(vertex, seen_vertex=None):
    if seen_vertex is None:
        seen_vertex = {}
    seen_vertex[vertex.value] = True
    print(vertex)
    for v in vertex.adjacent_vertices:
        if seen_vertex.get(v.value):
            continue
        dfs_traverse(v, seen_vertex)


def bfs_traverse(vertex):
    q = Queue(vertex)
    seen_vertex = {vertex.value: True}
    while len(q):
        current = q.dequeue()
        print(current)
        for v in current.adjacent_vertices:
            if seen_vertex.get(v.value):
                continue
            else:
                seen_vertex[v.value] = True
                q.enqueue(v)


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

print(alice)
dfs_traverse(alice)
print()
bfs_traverse(alice)
