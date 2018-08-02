# 6 nodes, 8 arcs
dict_d_graph = {'A': ['B', 'C'],
                'B': ['C', 'D'],
                'C': ['D'],
                'D': ['C'],
                'E': ['F'],
                'F': ['C']}


# finds the FIRST path from start node to end node
# nodes don't reoccur (no cycles)
def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        # if not graph.has_key(start):
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return None


# >>> find_path(graph, 'A', 'D')
#     ['A', 'B', 'C', 'D']
#     >>>
