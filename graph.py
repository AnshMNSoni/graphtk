import networkx as nx
from tkinter import simpledialog, messagebox
from tkinter import *
import matplotlib.pyplot as plt
import math


class Graph:
    def __init__(self):
        pass
    
    # printing adjacency_matrix
    def adjacency_matrix(self, G, is_directed=False):
        length = len(G.vertices)
        
        adj = {vertex: [] for vertex in G.vertices}
        
        try:
            for edge in G.edges:
                vertex1, vertex2 = edge[0], edge[1]
                adj[vertex1].append(vertex2)
                
                if not is_directed:
                    adj[vertex2].append(vertex1)
            
            adj_matrix = [[0 for _ in range(length)] for _ in range(length)]
      
            for i in range(length):
                for j in range(length):
                    cnt = adj[G.vertices[i]].count(G.vertices[j])
                    adj_matrix[i][j] = cnt
            
            return adj_matrix
        
        except TypeError:
            return
        
    
    # Calculating undirected Graph/Matrix edges
    def undi_edges(self, vertices):
        cnt = 0
        edges = []
        
        for i in vertices:
            for j in range(cnt, len(vertices)):
                self.window = Tk()    
                self.img = PhotoImage(file='./main_bg.png')
                self.window.label = Label(image=self.img)
                self.window.label.grid(row=0, column=0)
                
                num = simpledialog.askinteger("Input", "Enter the number of edges between " + i + "-" + vertices[j] + ": ")
                self.window.label = Label(text=num)
                self.window.label.grid(row=0, column=1)
                
                try:
                    if(num!=0):
                        if(i == vertices[j]):
                            edges.append((i, vertices[j]))
                        else:
                            for _ in range(num):
                                edges.append((i, vertices[j]))
                            
                except TypeError:
                    edges = None
                    messagebox.showerror(title="Try Again!", message="Edges cannot be empty.")
                finally:
                    self.window.destroy()
                    
            cnt += 1
        return edges
    
    
    # Calculating Undirected adjacency_matrix
    def undiMatrix(self, Graph, vertices):
        edges = self.undi_edges(vertices)
        
        G = Graph(vertices=vertices, edges=edges)
        
        matrix = self.adjacency_matrix(G)
        return matrix
    
    
    # Ploting Undirected Graph
    def undiGraph(self, vertices):
        edges = self.undi_edges(vertices)
        
        try:
            plotGraph = nx.Graph()
            plotGraph.add_nodes_from(vertices)
            plotGraph.add_edges_from(edges)
        
            nx.draw(plotGraph, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', font_size=15, font_weight='bold')
        
            plt.show()
        except TypeError:
            return
    
    
    # Calculating Directed Graph/Matrix edges
    def di_edges(self, vertices):
        edges = []
            
        for i in vertices:
            for j in range(len(vertices)):
                self.window = Tk()    
                self.img = PhotoImage(file='./main_bg.png')
                self.window.label = Label(image=self.img)
                self.window.label.grid(row=0, column=0)
                
                num = simpledialog.askinteger("Input", "Enter the number of edges between " + i + "-" + vertices[j] + ": ")
                self.window.label = Label(text=num)
                self.window.label.grid(row=0, column=1)
                
                try:
                    if(num!=0):
                        if(i == vertices[j]):
                            edges.append((i, vertices[j]))
                        else:
                            for _ in range(num):
                                edges.append((i, vertices[j]))
                            
                except TypeError:
                    edges = None
                    messagebox.showerror(title="Try Again!", message="Edges cannot be empty.")
                finally:
                    self.window.destroy()
                    
        return edges
    
    
    # Calculating Directed adjacency_matrix
    def diMatrix(self, Graph, vertices):
        edges = self.di_edges(vertices)
        
        G = Graph(vertices=vertices, edges=edges)
        
        matrix = self.adjacency_matrix(G, True)
        return matrix
            
    
    # Ploting Directed Graph
    def diGraph(self, vertices):
        edges = self.di_edges(vertices)
        
        try:
            plotGraph = nx.DiGraph()
            plotGraph.add_nodes_from(vertices)
            plotGraph.add_edges_from(edges)
        
            nx.draw(plotGraph, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', font_size=15, font_weight='bold')
        
            plt.show()
        except TypeError:
            return
        
    
    def weightMatrix(self, vertices):
        length = len(vertices)
        weight_matrix = [[0 for _ in range(length)] for _ in range(length)]
            
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                self.window = Tk()    
                self.img = PhotoImage(file='./main_bg.png')
                self.window.label = Label(image=self.img)
                self.window.label.grid(row=0, column=0)
                
                num = simpledialog.askinteger("Input", "Enter the distance require to travel from " + vertices[i] + " to " + vertices[j] + ": ")
                self.window.label = Label(text=num)
                self.window.label.grid(row=0, column=1)
                
                try:
                    if(num!=0):
                        weight_matrix[i][j] = num
                    else:
                        weight_matrix[i][j] = math.inf
                            
                except TypeError:
                    messagebox.showerror(title="Try Again!", message="Edges cannot be empty.")
                finally:
                    self.window.destroy()
                    
        return weight_matrix