import tkinter as tk
L = ["blue", "green", "black", "yellow", "magenta", "red"]
taille = 250
i = 0
root = tk.Tk()
canvas = tk.Canvas(root, bg = "gray", height = 500, width = 500)
canvas.grid()
while taille > 10:
    canvas.create_oval((250 - taille, 250 - taille),(250 + taille, 250 + taille), fill = L[i])
    if i == len(L)-1:
        i = 0
    else : 
        i += 1
    taille -= 10

root.mainloop()