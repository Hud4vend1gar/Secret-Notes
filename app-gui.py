import tkinter as tk
from PIL import Image


screen = tk.Tk()
screen.minsize(360,600)
screen.title("Secret Notes")

#? top-secret img
canvas = tk.Canvas(screen, width=360,height=200)
canvas.pack()
logo = tk.PhotoImage(file="top-secret2.png")
canvas.create_image((180,100),image=logo)



tk.mainloop()