from collections import namedtuple
from tkinter import *
from tkinter import simpledialog, messagebox
from graph import *
from matrix_gui import *

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
        self.label.grid(row=0, column=0, rowspan=4)
        
        self.undigraph = Button(text="Undirected Graph", command=self.to_undiGraph, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.undigraph.grid(row=0, column=0)
        
        self.undimatrix = Button(text="Undirected Matrix", command=self.to_undiMatrix, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.undimatrix.grid(row=1, column=0)
        
        self.digraph = Button(text="Directed Graph", command=self.to_diGraph, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.digraph.grid(row=2, column=0)
        
        self.dimatrix = Button(text="Directed Matrix", command=self.to_diMatrix, font=FONT, bg=BG, fg=FG, bd=3, highlightthickness=0)
        self.dimatrix.grid(row=3, column=0)
        
        self.window.mainloop()
        
        
    def to_undiGraph(self):
        try:
            self.destroyButtons()
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
        
    
    def to_diGraph(self):
        try:
            self.destroyButtons()
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
    
    
    def to_undiMatrix(self):
        try:
            self.destroyButtons()
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
    
    
    def to_diMatrix(self):
        try:
            self.destroyButtons()
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
        
        
    def destroyButtons(self):
        self.undigraph.destroy()
        self.digraph.destroy()
        self.undimatrix.destroy()
        self.dimatrix.destroy()
    
    
GUI()