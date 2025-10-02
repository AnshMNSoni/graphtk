from graphtk.edges import Edge
from graphtk.graphs import Graph
from graphtk.matrix import Matrices
from graphtk.graph_coloring import GraphColoring
from graphtk.adjacency_list import AdjacencyList

class Toolkit:
    def __init__(self):
        self.edge = Edge()
        self.graphs = Graph()
        self.matrices = Matrices()
        self.coloring = GraphColoring()
        self.show_graph = AdjacencyList()
    
    def main(self):
        pass
    
    # Methods in Edges
    def edges(self, vertices: list, is_directed: bool):
        return self.edge.edges(vertices, is_directed)
    
    # Methods in Graphs
    def paths(self, edges: list, vertices: list, is_directed):
        return self.graphs.paths(edges, vertices, is_directed)
    
    def trails(self, edges: list, vertices: list, is_directed):
        return self.graphs.trails(edges, vertices, is_directed)
    
    def cycle(self, edges: list, vertices: list, is_directed):
        return self.graphs.cycle(edges, vertices, is_directed)
    
    def simplepath(self, edges: list, vertices: list, is_directed):
        return self.graphs.simplepath(edges, vertices, is_directed)
    
    def is_path(self, edges: list, vertices: list, is_directed: bool, path: dict):
        return self.graphs.is_path(edges, vertices, is_directed, path)
    
    def is_trail(self, edges: list, vertices: list, is_directed: bool, trail: dict):
        return self.graphs.is_trail(edges, vertices, is_directed, trail)
    
    def is_cycle(self, edges: list, vertices: list, is_directed: bool, cycle: dict):
        return self.graphs.is_cycle(edges, vertices, is_directed, cycle)
    
    def is_simplepath(self, edges: list, vertices: list, is_directed: bool, path: dict):
        return self.graphs.is_simplepath(edges, vertices, is_directed, path)
    
    def is_traversable(self, edges: list, vertices: list, is_directed: bool):
        return self.graphs.is_traversable(edges, vertices, is_directed)
    
    def is_euler(self, edges: list, vertices: list, is_directed: bool):
        return self.graphs.is_euler(edges, vertices, is_directed)
    
    def is_hamilton(self, edges: list, vertices: list, is_directed: bool):
        return self.graphs.is_hamilton(edges, vertices, is_directed)
    
    def is_complete(self, edges: list, vertices: list, is_directed: bool):
        return self.graphs.is_complete(edges, vertices, is_directed)
    
    def is_regular(self, edges: list, vertices: list, is_directed: bool):
        return self.graphs.is_regular(edges, vertices, is_directed)
    
    def is_bipartite(self, edges: list, vertices: list, is_directed: bool):
        return self.graphs.is_bipartite(edges, vertices, is_directed)
    
    def is_planner(self, edges: list, vertices: list, is_directed: bool):
        return self.graphs.is_planner(edges, vertices, is_directed)
    
    # Methods in Matrices
    def adjacency_matrix(self, edges: list, vertices: list, is_directed: bool):
        return self.matrices.adjacency_matrix(edges, vertices, is_directed)
    
    def weight_matrix(self, edges: list, vertices: list, is_directed: bool = None):
        return self.matrices.weight_matrix(edges, vertices, is_directed)
    
    def b_matrix(self, edges: list, vertices: list, is_directed: bool = None):
        return self.matrices.b_matrix(edges, vertices, is_directed)
    
    def path_matrix(self, edges: list, vertices: list, is_directed: bool = None):
        return self.matrices.path_matrix(edges, vertices, is_directed)
    
    # Methods in Graph Coloring
    def vertex_coloring(self, edges: list, vertices: list, is_directed: bool = None):
        return self.coloring.vertex_coloring(edges, vertices, is_directed)
    
    # Methods in Adjacency List
    def adjacency_list(self, edges: list, vertices: list, is_directed: bool):
        return self.show_graph.adjacency_list(edges, vertices, is_directed)
    