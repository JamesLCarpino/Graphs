from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # visit all nodes
    visited = set()
    # initialize the Queue
    queue = Queue()
    # enqueue the ancestor
    queue.enqueue([ancestors])
    # loop through while the queue is not zero
    while queue.size() > 0:
        # make the path
        path = queue.dequeue()
        # find the last node in the path
        ancestoral_node = path[-1]  # maybe this will be [0]

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

