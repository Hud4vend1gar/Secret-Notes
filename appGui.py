import tkinter as tk
from PIL import Image
#import cryptographyy


screen = tk.Tk()
screen.minsize(360,600)
screen.maxsize(360,600)
screen.title("Secret Notes")

#? top-secret img
canvas = tk.Canvas(screen, width=360,height=200)
canvas.pack()
logo = tk.PhotoImage(file="top-secret2.png")
canvas.create_image((180,100),image=logo)

#?variables
label_font = "Calibri 12 bold"

#? labels and entrys
title_frame = tk.Frame(pady=5)
title_frame.pack()
title_label = tk.Label(master=title_frame,text="Enter your title",font=label_font)
title_entry = tk.Entry(master=title_frame,width=40)
title_label.pack()
title_entry.pack()

secret_frame = tk.Frame(pady=5)
secret_frame.pack()
secret_label = tk.Label(master=secret_frame,text="Enter your secret note",font=label_font)
secret_entry = tk.Text(master=secret_frame,height=10,width=35)
secret_label.pack()
secret_entry.pack()

key_frame = tk.Frame(pady=5)
key_frame.pack()
key_label = tk.Label(master=key_frame,text="Enter master key",font=label_font)
key_entry = tk.Entry(master=key_frame,width=40)
key_label.pack()
key_entry.pack()

#? buttons
encrypt_button = tk.Button(text="Save & Encrypt",font="Arial 10 normal")
decrypt_button = tk.Button(text="Decrypt",font="Arial 10 normal")
encrypt_button.pack(pady=5)
decrypt_button.pack()


#? functions




tk.mainloop()