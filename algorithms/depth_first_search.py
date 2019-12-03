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

from collections import deque

def depth_first_search_route(graph, start_node, end_node, route = deque(), tried = []):

    while start_node != end_node:
        if start_node not in route:
            route.append(start_node)
            for sub_node in graph[start_node]:
                print(route,  "new")
                depth_first_search_route(graph, sub_node, end_node, route, tried)
        elif start_node not in tried:
            tried.append(start_node)
            route.pop()
            print(route, "same")
            depth_first_search_route(graph, route[-1], end_node, route, tried)
    route.append(end_node)
    return route

print(depth_first_search_route(graph1,"A", "F"))



    #if start_node not in route:
#        route = route.append(start_node)
#
#    if start_node == end_node:
#        return True
#    elif start_node in discovered:
#        return False
#    else:
#        discovered.append(start_node)
#        for new_node in graph[start_node]:
#            print(discovered)
#            depth_first_search_route(graph, new_node,end_node)
#    return False
#

#print(depth_first_search_route(graph1, "A", "D"))
