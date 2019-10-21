# Given node order
#            A
#          / \
#         /   \
#        /     \
#       B       C
#      /|\      / \
#     / | \    /   \
#    D  E  F   S    T
#   /  /\     /
#  G  H  I   U

# Expected order of nodes
#            1
#          / \
#         /   \
#        /     \
#       2       9
#      /|\      / \
#     / | \    /   \
#    3  5  8  10    12
#   /  /\     |
#  4  6  7   11

graph1 = {
        "A":["B","C"],
        "B":["A","D","E","F"],
        "C":["A","S","T"],
        "D":["B","G"],
        "E":["B","H","I"],
        "F":["B"],
        "G":["D"],
        "H":["E"],
        "I":["E"],
        "S":["C","U"],
        "T":["C"],
        "U":["S"]
        }

def depth_first_search(graph, node, discovered=[]):
    if node not in discovered:
        discovered.append(node)
        for sub_node in graph[node]:
            depth_first_search(graph, sub_node, discovered)
    return discovered

print(depth_first_search(graph1,"A"))
