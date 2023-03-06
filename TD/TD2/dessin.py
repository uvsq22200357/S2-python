import tkinter as tk
from random import randint
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
c = " "
def cercle():
    global c
    a = randint(0, 600)
    b = randint(0,600)
    if c == " ":
        canvas.create_oval(a, b, a+100, b+100, fill = "blue")
    else:
        canvas.create_oval(a, b, a+100, b+100, fill = c)
def carré():
    global c
    a = randint(0, 600)
    b = randint(0,600)
    if c == " ":
        canvas.create_rectangle(a, b, a+100, b+100, fill = "red")
    else : 
        canvas.create_rectangle(a, b, a+100, b+100, fill = c)

def croix():
    global c
    a = randint(0, 600)
    b = randint(0,600)
    if c == " ":
        canvas.create_line(a, b, a+100, b+100, fill = "yellow", width = 5)
        canvas.create_line(a+100, b, a, b+100, fill = "yellow", width = 5)
    else:
        canvas.create_line(a, b, a+100, b+100, fill = c, width = 5)
        canvas.create_line(a+100, b, a, b+100, fill = c, width = 5)
def couleur():
    global c
    c = input("Saisir couleur:")




root = tk.Tk()
root.config(bg = "#aaaaaa")


bouton_2 = tk.Button(root, text = "Cercle", bg = "#aaaaaa", command = cercle)
bouton_3 = tk.Button(root, text = "Carré", bg = "#aaaaaa", command = carré)
bouton_4 = tk.Button(root, text = "Croix", bg = "#aaaaaa", command = croix)
bouton_2.grid(row= 1)
bouton_3.grid(row= 2)
bouton_4.grid(row= 3)
bouton_1 = tk.Button(root, text = "Choisir couleur",  bg = "#aaaaaa", command = couleur
)
bouton_1.grid(row = 0, column = 1)
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "gray", relief = "raised", borderwidth = "10")
canvas.grid(column= 1, row = 1, rowspan = 3)



root.mainloop()