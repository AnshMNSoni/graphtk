import networkx as nx
from tkinter import simpledialog, messagebox
from tkinter import *
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        pass
    
    def adjacency_matrix(self,G):
        length = len(G.vertices)
        
        adj = {vertex: [] for vertex in G.vertices}
        
        try:
            for edge in G.edges:
                vertex1, vertex2 = edge[0], edge[1]
                adj[vertex1].append(vertex2)
                adj[vertex2].append(vertex1)  
            print(adj)
            adj_matrix = [[0 for _ in range(length)] for _ in range(length)]
            
            for i in range(length):
                for j in range(length):
                    cnt = adj[G.vertices[i]].count(G.vertices[j])
                    adj_matrix[i][j] = cnt
            
            return adj_matrix
        except TypeError:
            return

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
                    return
                finally:
                    self.window.destroy()
                    
            cnt += 1
        return edges
    
    
    def undiMatrix(self, Graph, vertices):
        edges = self.undi_edges(vertices)
        
        G = Graph(vertices=vertices, edges=edges)
        
        matrix = self.adjacency_matrix(G)
        return matrix
    
            
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
    
    
    def diMatrix(self, Graph, vertices):
        edges = self.di_edges(vertices)
        
        G = Graph(vertices=vertices, edges=edges)
        
        matrix = self.adjacency_matrix(G)
        return matrix
            
    
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