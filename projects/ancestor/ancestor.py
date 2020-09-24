# describe problem in graph terminology
# DAG - directed acyclical graph
## node = ancestor
## edge = parent/child

# which algorithm?
## BFT, DFT, BFS, DFSearch

# Search or traversal?
## BF --> shortest path strait to root
## DF --> heads to leaves first
## more like traversal because must travel/ compare every path from starting person to earliest ancestor

## DF can be recursive, but not BF

import sys
sys.path.insert(0, '/Users/user/Desktop/LambdaPT9/Graphs/projects/graph')
from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node, distance=0):
    lineage_graph = Graph()
    stack = Stack()
    stack.push(starting_node)
    visited = set()
    # earliest_ancestors = [(path, earliest ancestor)]
    earliest_ancestors = []
    path = []

    # create graph
    for (parent, child) in ancestors:
        # add verticies
        lineage_graph.add_vertex(parent)
        lineage_graph.add_vertex(child)
        # add edges
        lineage_graph.add_edge(child, parent)

    # run DFT, track
    while stack.size() > 0:
        print('stack size', stack.size())
        curr_anc = stack.pop()
        print('curr_anc', curr_anc)
        print(f'{curr_anc} in visited? -> {visited}')
        print('stack size after pop', stack.size())
        if curr_anc not in visited:
            visited.add(curr_anc)
            print(f'{curr_anc} in visited NOW? -> {visited}')
            path.append(curr_anc)
            print('path', path)
            print('parent(s)', lineage_graph.vertices[curr_anc])
            for parents in lineage_graph.get_neighbors(curr_anc):
                stack.push(parents)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(test_ancestors, 1), '-> 10?')
# print(earliest_ancestor(test_ancestors, 2), '-> -1?')
# print(earliest_ancestor(test_ancestors, 3), '-> 10?')
# print(earliest_ancestor(test_ancestors, 4), ' -> -1?')
# print(earliest_ancestor(test_ancestors, 5), '-> 4?')
print(earliest_ancestor(test_ancestors, 6), '-> 10?')
# print(earliest_ancestor(test_ancestors, 7), '-> 4?')
# print(earliest_ancestor(test_ancestors, 8), '-> 4?')
# print(earliest_ancestor(test_ancestors, 9), '-> 4?')
# print(earliest_ancestor(test_ancestors, 10), '-> -1?')
# print(earliest_ancestor(test_ancestors, 11), '-> -1?')