"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")
            print("You fool! There is no starting point!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        queue = Queue()
        # Create a set to store the visited nodes
        visited = set()
        # Init: enqueue the starting node
        queue.enqueue(starting_vertex)
        # While the queue isn't empty
        while queue.size() > 0:
            # Dequeue the first item
            vertex = queue.dequeue()
            # If it's not been visited:
            if vertex not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(vertex)
                # Do something with the node
                print(vertex)
                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(vertex):
                    queue.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Create a set to store the visited nodes
        visited = set()
        # Init: push the starting node
        s.push(starting_vertex)
        # While the stack isn't empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)
                # Do something with the node
                print(v)
                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        print(starting_vertex)
        if visited is None:
            visited = set()
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        # mark s as visited
        # for all neighbours w of s in Graph G:
        #     if w is not visited:
        #         DFS-recursive(G, w)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = []
        path = queue.enqueue([starting_vertex])
        while queue.size() > 0:
            first_path = queue.dequeue()
            last_vertex = first_path[-1]
            if last_vertex not in visited:
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = list(first_path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)
                    if neighbor == destination_vertex:
                        return new_path
                visited.append(path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = []
        path = stack.push([starting_vertex])
        while stack.size() > 0:
            first_path = stack.pop()
            last_vertex = first_path[-1]
            if last_vertex not in visited:
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = list(first_path)
                    new_path.append(neighbor)
                    stack.push(new_path)
                    if neighbor == destination_vertex:
                        return new_path
                visited.append(path)

    def dfs_recursive(
        self, starting_vertex, destination_vertex, visited=None, path=None
    ):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
            path = [starting_vertex]
            # visited.add(starting_vertex)
        # marks the first one

        # last node in the current path
        last_path = path[-1]
        # base case: if the starting vertex == destination that is the smalles route possible
        if last_path == destination_vertex:
            # return whole path
            return path
        # check and make sure that last path is not visited
        if last_path not in visited:
            visited.add(last_path)

            for neighbor in self.get_neighbors(last_path):
                new_path = list(path)
                new_path.append(neighbor)

                return_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path
                )
                # because return none in else statement
                if return_path is not None:
                    return return_path
        else:
            return None


#         1. Mark the current node as visited(initially current node is the root node)
#         2. Check if current node is the goal, If so, then return it.
#         3. Iterate over children nodes of current node, and do the following:
#               1. Check if a child node is not visited.
#               2. If so, then, mark it as visited.
#               3. Go to it's sub tree recursively until you find the goal node(In other words, do the same steps here passing the child node as the current node in the next recursive call).
#               4. If the child node has the goal node in this sub tree, then, return it.
#         3. If goal node is not found, then goal node is not in the tree!


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    # print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
