class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


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

    def bft(self, starting_vertex_id):
        # create an empty queue that we will start at
        q = Queue()

        # create a set for the visited nodes
        visisted = set()
        # init: enqueue the starting node
        q.enqueue(starting_vertex_id)
        # while the queue isn't empty
        while q.size() > 0:
            #  deque the first item
            v = q.dequeue()
            #  if it hasn't been visisted
            if v not in visisted:
                # add it to the visisted
                visisted.add(q)
                print(f"Visisted {v}")
                # all all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "A")
g.add_edge("B", "C")
g.add_edge("B", "B")
g.add_edge("C", "D")
g.add_edge("D", "C")

g.bft("B")
# order: B, then A, C, then D (THIS IS BASED OFF OF THE TREE DRAWN IN CLASSLECTURE)
# print(g.bft)
# self.verticies = {
#     'A':{B, C}
# }
