# 4 color theorm

from graph_init import namedtuple

class GraphColoring:
    def __init__(self):
        pass
    
    def vertex_coloring(self, edges: list, vertices: list, is_directed: bool = None):
        G = namedtuple(edges, vertices, False)
        result = {}

        for u in G.keys():
            neighbor_colors = set()

            for neighbor in G[u]:
                if neighbor in result:
                    neighbor_colors.add(result[neighbor])

            # find the smallest available color
            color = 0
            while color in neighbor_colors:
                color += 1
            result[u] = color
        return result
