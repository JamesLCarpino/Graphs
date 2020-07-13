class Graph:
    # neighbors are nodes directly connected to the node (that you're looking at)
    # imediatly adjacent
    def __init__(self):
        self.verticies = {
            # this dic will keep track of neighbors for a vert
        }

    def add_vertex(self, vertex_id):
        self.verticies[vertex_id] = set()  # this will hold edges

    def add_edge(self, v1, v2):
        # v1 is from, v2 is to
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)  # there's an edge from v1 to v2
        else:
            raise IndexError("Verticies does not exsist")

    def get_neighbors(self, vertex_id):
        return self.verticies[vertex_id]


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "A")
g.add_edge("B", "C")
g.add_edge("B", "B")

print(g.verticies)
# self.verticies = {
#     'A':{B, C}
# }
