from tkinter import *

FONT = ('Times New Roman', 20, 'bold')
FG = '#161D6F'
BG1 = '#F5F4B3'
BG2 = '#B9E5E8'

def display_matrix(matrix):
    try:
        window = Tk()
        window.title("Adjacency Matrix")
        window.config(padx=50, pady=50, bg=BG1)
    
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                label = Label(text=matrix[i][j], fg=FG, bg=BG2, font=FONT, borderwidth=5, relief='ridge', width=10, height=2)
                label.config(padx=20, pady=20)
                label.grid(row=i, column=j)
                
        window.mainloop()
    except TypeError:
        window.destroy()
        return