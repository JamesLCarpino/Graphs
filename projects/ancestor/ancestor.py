from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_node):
    # build a graph
    graph = Graph()
    # go over a set of vertices and make nodes
    for pair in ancestors:
        # create the vertexes
        # for the specific id
        # create and check to see if its already in
        if pair[0] not in graph.vertices:
            graph.add_vertex(pair[0])
        if pair[1] not in graph.vertices:
            graph.add_vertex(pair[1])
        # create the edges
        graph.add_edge(pair[1], pair[0])

    # initialize queue
    queue = Queue()
    queue.enqueue([starting_node])
    # keep track of the longest path to figure out
    longest_path = []

    while queue.size() > 0:
        vertex_path = queue.dequeue()

        if len(vertex_path) > len(longest_path):
            longest_path = vertex_path
        if len(vertex_path) == len(longest_path):
            if vertex_path[-1] < longest_path[-1]:
                longest_path = vertex_path

        for neighbors in graph.get_neighbors(vertex_path[-1]):
            temp_path = vertex_path.copy()
            temp_path.append(neighbors)
            queue.enqueue(temp_path)
    if len(longest_path) <= 1:
        return -1
    else:
        return longest_path[-1]

    # # visit all nodes
    # visited = set()
    # # initialize the Queue
    # queue = Queue()
    # # enqueue the ancestor
    # queue.enqueue([ancestors])
    # # loop through while the queue is not zero
    # while queue.size() > 0:
    #     # make the path
    #     path = queue.dequeue()
    #     # find the last node in the path
    #     ancestoral_node = path[-1][0]  # maybe this will be [0]
    #     # if the ancestor is not in the set
    #     if ancestoral_node not in visited:
    #         # add the ancestoral node to the set
    #         visited.add(ancestoral_node)
    #         # if the ancestoral node is the starting node it is the ancestor
    #         if ancestoral_node == starting_node:
    #             return ancestoral_node
    #         #
    # return None

    # use traversal not search


# def get_neighbors(ancestor):
#     neighbors = []
#     family_tree = list(ancestor)
#     for i in range(len(family_tree)):
#         for branch in letters:
#             temp_tree = list(family_tree)
#             temp_tree[i] = branch
#             t = "".join(temp_tree)
#             if t == ancestor:
#                 continue
#             if t in family_tree:
#                 neighbors.append(t)
#     return neighbors

# -> make a set that holds all paths of the graph

#     ->similar to how you did the breadthFirst search for quickest path
# -> loop through that set:
#     -> if the path's child has a parent,
#         -> set the parent to be the child
#         -> check to see if that child has a parent
#         -> if this parent that was no changed to a child DOES NOT HAVE A PARENT ASSCIATED:
#             -> that is the ancestor node of the original input
#             -> return the node
#         -> if it DOES have a parent:
#             -> repeat previous steps


"""
Psuedo Code Notes:

graph structure:
10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9



U:
given a node, find the ancestor node.
the node will be connected by a path to another node.
that node is the parent node
use the parent node that you are now on to search if there is a path to another node
that node is the ancestor node, if it has no other parent nodes.


P:
    -> make a set that holds all paths of the graph
        ->similar to how you did the breadthFirst search for quickest path
    -> loop through that set: 
        -> if the path's child has a parent, 
            -> set the parent to be the child
            -> check to see if that child has a parent
            -> if this parent that was no changed to a child DOES NOT HAVE A PARENT ASSCIATED:
                -> that is the ancestor node of the original input
                -> return the node
            -> if it DOES have a parent:
                -> repeat previous steps
                







"""

