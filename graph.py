import networkx as nx
from tkinter import simpledialog
import matplotlib.pyplot as plt


def adjacency_matrix(G):
    length = len(G.vertices)
    
    adj = {vertex: [] for vertex in G.vertices}
    for edge in G.edges:
        vertex1, vertex2 = edge[0], edge[1]
        adj[vertex1].append(vertex2)
        adj[vertex2].append(vertex1)  
        
    adj_matrix = [[0 for _ in range(length)] for _ in range(length)]
    
    for i in range(length):
        for j in range(length):
            cnt = adj[G.vertices[i]].count(G.vertices[j])
            adj_matrix[i][j] = cnt
     
    return adj_matrix


def undi_edges(vertices):
    cnt = 0
    edges = []
    
    for i in vertices:
        for j in range(cnt, len(vertices)):
            num = simpledialog.askinteger("Input", "Number of edges between " + i + "-" + vertices[j] + ": ")
            
            for _ in range(num):
                edges.append((i, vertices[j]))
        cnt += 1
    return edges


def undiMatrix(Graph, vertices):
    edges = undi_edges(vertices)
    
    G = Graph(vertices=vertices, edges=edges)
    
    matrix = adjacency_matrix(G)
    return matrix

        
def undiGraph(vertices):
    edges = undi_edges(vertices)
    
    plotGraph = nx.Graph()
    plotGraph.add_nodes_from(vertices)
    plotGraph.add_edges_from(edges)

    nx.draw(plotGraph, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', font_size=15, font_weight='bold')

    plt.show()


def di_edges(vertices):
    edges = []
        
    for i in vertices:
        for j in range(len(vertices)):
            num = simpledialog.askinteger("Input", "Number of edges between " + i + "-" + vertices[j] + ": ")
            
            for _ in range(num):
                edges.append((i, vertices[j]))
    return edges


def diMatrix(Graph, vertices):
    edges = di_edges(vertices)
    
    G = Graph(vertices=vertices, edges=edges)
    
    matrix = adjacency_matrix(G)
    return matrix
        

def diGraph(vertices):
    edges = di_edges(vertices)
    
    plotGraph = nx.DiGraph()
    plotGraph.add_nodes_from(vertices)
    plotGraph.add_edges_from(edges)

    nx.draw(plotGraph, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', font_size=15, font_weight='bold')

    plt.show()