from collections import namedtuple
from tkinter import *
from tkinter import simpledialog, messagebox
from graph import *
from matrix_gui import *
from sympy import Matrix
import math

FONT = ('Times New Roman', 16, 'bold')
FG = '#161D6F'
BG = '#F5F4B3'

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Graph Theory")
        self.Graph = namedtuple('Graph', ['vertices', 'edges'])
        
        self.img = PhotoImage(file='./main_bg.png')
        self.label = Label(image=self.img)
        self.label.config(width=1000, height=600)
        self.label.grid(row=0, column=0, columnspan=2)
        
        self.undigraph = Button(text="Undirected Graph Analysis", command=self.to_undiGraph, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.undigraph.grid(row=0, column=0)
        
        self.digraph = Button(text="Directed Graph Analysis", command=self.to_diGraph, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.digraph.grid(row=0, column=1)
        
        self.window.mainloop()
        
     
    #  Undirected Graph    
    def to_undiGraph(self):
            self.destroyMainPageButtons()
            self.window.destroy()
            UndirectedGUI()
        
    def inside_undiGraph(self):
        try:    
            user = simpledialog.askstring("Input", "Enter the vertices of the Graph:\n\nNote: Leave empty space while entering vertices\n\nExample: A B C").upper().split()
            
            if(user != []):
                vertices = list(user)
                self.window.destroy()
                Graph().undiGraph(vertices)
            else:
                messagebox.showwarning(title="Empty Space Found", message="Please, enter atleast one vertex!")
                self.window.destroy()
                GUI()
            
        except AttributeError:
            messagebox.showerror(title="Try again", message="Something went wrong.")
            self.window.destroy()
            GUI()
        
    
    # Directed Graph 
    def to_diGraph(self):
        self.destroyMainPageButtons()
        self.window.destroy()
        DirectedGUI()
    
    def inside_diGraph(self):
        try:
            user = simpledialog.askstring("Input", "Enter the vertices of the Graph:\n\nNote: Leave empty space while entering vertices\n\nExample: A B C").upper().split()
            
            if(user != []):
                vertices = list(user)
                self.window.destroy()
                Graph().diGraph(vertices)
            else:
                messagebox.showwarning(title="Empty Space Found", message="Please, enter atleast one vertex!")
                self.window.destroy()
                GUI()
            
        except AttributeError:
            messagebox.showerror(title="Try again", message="Something went wrong.")
            self.window.destroy()
            GUI()
            
    # Undirected Matrix
    def to_undiMatrix(self):
        self.destroyMainPageButtons()
        self.window.destroy()
        UndirectedGUI()
    
    def inside_undiMatrix(self):
        try:
            user = simpledialog.askstring("Input", "Enter the vertices of the Graph:\n\nNote: Leave empty space while entering vertices\n\nExample: A B C").upper().split()
            
            if(user != []):
                vertices = list(user)
                self.window.destroy()
                matrix = Graph().undiMatrix(self.Graph, vertices)
                display_matrix(matrix)
            else:
                messagebox.showwarning(title="Empty Space Found", message="Please, enter atleast one vertex!")
                self.window.destroy()
                GUI()
                
        except AttributeError:
            messagebox.showerror(title="Try again", message="Something went wrong.")
            self.window.destroy()
            GUI()
    
    
    # Directed Matrix 
    def to_diMatrix(self):
        self.destroyMainPageButtons()
        self.window.destroy()
        DirectedGUI()
    
    def inside_diMatrix(self):
        try:
            user = simpledialog.askstring("Input", "Enter the vertices of the Graph:\n\nNote: Leave empty space while entering vertices\n\nExample: A B C").upper().split()
            
            if(user != []):
                vertices = list(user)
                self.window.destroy()
                matrix = Graph().diMatrix(self.Graph, vertices)
                display_matrix(matrix)
            else:
                messagebox.showwarning(title="Empty Space Found", message="Please, enter atleast one vertex!")
                self.window.destroy()
                GUI()
            
        except AttributeError:
            messagebox.showerror(title="Try again", message="Something went wrong.")
            self.window.destroy()
            GUI()
            
    
    # Directed B-Matrix
    def to_di_BMatrix(self):
        try:
            user = simpledialog.askstring("Input", "Enter the vertices of the Graph:\n\nNote: Leave empty space while entering vertices\n\nExample: A B C").upper().split()
            
            if(user != []):
                vertices = list(user)
                self.window.destroy()
                
                B_matrix = Graph().diMatrix(self.Graph, vertices)
                
                for _ in range(len(vertices)-1):
                    A = Matrix(B_matrix)
                    B = Matrix(B_matrix)
                    C = (A*B).tolist()
                    
                    for i in range(len(vertices)):
                        for j in range(len(vertices)):
                            B_matrix[i][j] = B_matrix[i][j] + C[i][j]
                    
                    A = C
                    
                display_matrix(B_matrix, 'B-Matrix')
                    
            else:
                messagebox.showwarning(title="Empty Space Found", message="Please, enter atleast one vertex!")
                self.window.destroy()
                GUI()
            
        except AttributeError:
            messagebox.showerror(title="Try again", message="Something went wrong.")
            self.window.destroy()
            GUI()
    
    
    # Path Matrix:
    def to_pathMatrix(self):
        try:
            user = simpledialog.askstring("Input", "Enter the vertices of the Graph:\n\nNote: Leave empty space while entering vertices\n\nExample: A B C").upper().split()
            
            if(user != []):
                vertices = list(user)
                self.window.destroy()
                
                B_matrix = Graph().diMatrix(self.Graph, vertices)
                
                for _ in range(len(vertices)-1):
                    A = Matrix(B_matrix)
                    B = Matrix(B_matrix)
                    C = (A*B).tolist()
                    
                    for i in range(len(vertices)):
                        for j in range(len(vertices)):
                            B_matrix[i][j] = B_matrix[i][j] + C[i][j]
                    
                    A = C
                
                for i in range(len(vertices)):
                    for j in range(len(vertices)):
                        if(B_matrix[i][j]!=0):
                            B_matrix[i][j] = 1
                
                display_matrix(B_matrix, 'Path-Matrix')
                    
            else:
                messagebox.showwarning(title="Empty Space Found", message="Please, enter atleast one vertex!")
                self.window.destroy()
                GUI()
            
        except AttributeError:
            messagebox.showerror(title="Try again", message="Something went wrong.")
            self.window.destroy()
            GUI()
            
    
    # Weight Matrix:
    def to_weightMatrix(self):
        try:
            user = simpledialog.askstring("Input", "Enter the vertices of the Graph:\n\nNote: Leave empty space while entering vertices\n\nExample: A B C").upper().split()
            
            if(user != []):
                vertices = list(user)
                self.window.destroy()
                
                matrix = Graph().weightMatrix(vertices)
                
                for k in range(len(vertices)):
                    for i in range(len(vertices)):
                        for j in range(len(vertices)):
                            matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
                
                for i in range(len(vertices)): 
                    for j in range(len(vertices)):
                        if(matrix[i][j] == math.inf):
                            matrix[i][j] = 0
                            
                display_matrix(matrix, 'Weight-Matrix')
                    
            else:
                messagebox.showwarning(title="Empty Space Found", message="Please, enter atleast one vertex!")
                self.window.destroy()
                GUI()
            
        except AttributeError:
            messagebox.showerror(title="Try again", message="Something went wrong.")
            self.window.destroy()
            GUI()
        
        
        
    def destroyMainPageButtons(self):
        self.undigraph.destroy()
        self.digraph.destroy()
    

class UndirectedGUI(GUI):
    def __init__(self):
        self.window = Tk()
        self.window.title("Graph Theory")
        self.Graph = namedtuple('Graph', ['vertices', 'edges'])
        
        self.img = PhotoImage(file='./main_bg.png')
        self.label = Label(image=self.img)
        self.label.config(width=1000, height=600)
        self.label.grid(row=0, column=0, columnspan=2)
        
        self.undigraph = Button(text="Graph Visualisation", command=super().inside_undiGraph, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.undigraph.grid(row=0, column=0)
        
        self.undimatrix = Button(text="Adjacency Matrix", command=super().inside_undiMatrix, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.undimatrix.grid(row=0, column=1)

        self.window.mainloop()
        

class DirectedGUI(GUI):
    def __init__(self):
        self.window = Tk()
        self.window.title("Graph Theory")
        self.Graph = namedtuple('Graph', ['vertices', 'edges'])
        
        self.img = PhotoImage(file='./main_bg.png')
        self.label = Label(image=self.img)
        self.label.config(width=1000, height=600)
        self.label.grid(row=0, column=0, columnspan=3,rowspan=2)
        
        self.undigraph = Button(text="Graph Visualisation", command=super().inside_diGraph, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.undigraph.grid(row=0, column=0)
        
        self.undimatrix = Button(text="Adjacency Matrix", command=super().inside_diMatrix, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.undimatrix.grid(row=0, column=1)
        
        self.BMatrix = Button(text="B-Matrix", command=super().to_di_BMatrix, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.BMatrix.grid(row=0, column=2)
        
        self.pathMatrix = Button(text="Path Matrix", command=super().to_pathMatrix, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.pathMatrix.grid(row=1, column=0)
        
        self.weightMatrix = Button(text="Weight Matrix", command=super().to_weightMatrix, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.weightMatrix.grid(row=1, column=1)
        
        self.window.mainloop()
    
GUI()