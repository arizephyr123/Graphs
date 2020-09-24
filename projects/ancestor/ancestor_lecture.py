def getParents(ancestors, node):
    for pair in ancestors:




def dft_recursive (ancestors, node, distance):
    parents = getParents(node)
    
    earliest = (node, distance)

    for parent in parents:
        pair = dft_recursive(ancestors, parent, distance +1)
        if pair[1] > earliest[1]:
            earliest = pair

    return earliest


def earliest_ancestor(ancestors, starting_node, distance=0):
    earliest = dft_recursive(ancestors, starting_node, distance)
    
    return earliest


    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(test_ancestors, 1), '-> 10?')
# print(earliest_ancestor(test_ancestors, 2), '-> -1?')
# print(earliest_ancestor(test_ancestors, 3), '-> 10?')
# print(earliest_ancestor(test_ancestors, 4), ' -> -1?')
# print(earliest_ancestor(test_ancestors, 5), '-> 4?')
print(earliest_ancestor(test_ancestors, 6), '-> 10?')