from tkinter import *

def display_matrix(matrix):
    window = Tk()
    window.title("Matrix")
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            label = Label(text=matrix[i][j])
            label.grid(row=i, column=j)
            
    window.mainloop()