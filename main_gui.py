from collections import namedtuple
from tkinter import *
from tkinter import simpledialog
from graph import *
from matrix_gui import *

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Graph Theory")
        self.window.config(width=500, height=300)
        
        self.Graph = namedtuple('Graph', ['vertices', 'edges'])
        
        undigraph = Button(text="Undirected Graph", command=self.to_undiGraph)
        undigraph.grid(row=0, column=0)
        
        undimatrix = Button(text="Undirected Matrix", command=self.to_undiMatrix)
        undimatrix.grid(row=0, column=1)
        
        digraph = Button(text="Directed Graph", command=self.to_diGraph)
        digraph.grid(row=1, column=0)
        
        dimatrix = Button(text="Directed Matrix", command=self.to_diMatrix)
        dimatrix.grid(row=1, column=1)
        
        self.window.mainloop()
        
        
    def to_undiGraph(self):
        self.window.destroy()
        user = simpledialog.askstring("Input", "Enter the vertices of the Graph: ").upper().split()
        vertices = list(user)
        
        undiGraph(vertices)
        
    
    def to_diGraph(self):
        self.window.destroy()
        user = simpledialog.askstring("Input", "Enter the vertices of the Graph: ").upper().split()
        vertices = list(user)
        
        diGraph(vertices)
    
    
    def to_undiMatrix(self):
        self.window.destroy()
        user = simpledialog.askstring("Input", "Enter the vertices of the Graph: ").upper().split()
        vertices = list(user)
        
        matrix = undiMatrix(self.Graph, vertices)
        display_matrix(matrix)
    
    def to_diMatrix(self):
        self.window.destroy()
        user = simpledialog.askstring("Input", "Enter the vertices of the Graph: ").upper().split()
        vertices = list(user)
        
        matrix = diMatrix(self.Graph, vertices)
        display_matrix(matrix)
    
GUI()