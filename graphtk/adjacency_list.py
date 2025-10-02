from graphtk.graph_init import namedtuple

class AdjacencyList:
    def __init__(self):
        pass
    
    def adjacency_list(self, edges: list, vertices: list, is_directed: bool):
        adj = namedtuple(edges, vertices, is_directed)  
        
        adj_list = {}
        for v in vertices:
            counts = {}
            for neighbor in adj[v]:
                counts[neighbor] = counts.get(neighbor, 0) + 1     
            adj_list[v] = [(k, counts[k]) for k in counts]
        return adj_list
