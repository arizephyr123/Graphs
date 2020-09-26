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

from util import Stack

def earliest_ancestor(ancestors, starting_node):
    # ancestors = [(parent, child), ...]
    # ancestor_hashmap = {ancestor/parent: set of children}
    ancestor_hashmap = {}
    for (parent, child) in ancestors:
        # parent = parent, child = child
        # if either ancestor not already in dict, then create entry with empty set as value
        if parent not in ancestor_hashmap:
            ancestor_hashmap[parent] = set()
        if child not in ancestor_hashmap:
            ancestor_hashmap[child] = set()
        # add children into sets
        ancestor_hashmap[parent].add(child)
    return dft(starting_node, ancestor_hashmap)


def dft(starting_node, ancestors):
    stack = Stack()
    stack.push([starting_node])
    visited = set()

    earliest_anc = -1

    while stack.size():
        curr_path 


    return earliest_anc



    


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