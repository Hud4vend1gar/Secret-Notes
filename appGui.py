import tkinter as tk
from PIL import Image
from cryptographyFuncs import *

screen = tk.Tk()
screen.minsize(360,600)
screen.maxsize(360,600)
screen.title("Secret Notes")

#? functions
def save_encrypt():
    text_title = title_entry.get()
    text_note = secret_entry.get(1.0,tk.END)
    text_password = key_entry.get()
    encrypt_text(text_title,text_note,text_password)
    title_entry.delete(first=0,last=tk.END)
    secret_entry.delete(1.0,tk.END)
    key_entry.delete(first=0,last=tk.END)

def decrypt_command():
    token = secret_entry.get(1.0,tk.END)
    password = key_entry.get()
    decrypted_text = decrypt_text(token,password)
    key_entry.delete(first=0,last=tk.END)  
    secret_entry.delete(1.0,tk.END)  
    title_entry.delete(first=0,last=tk.END)
    secret_entry.insert(1.0,decrypted_text)
    

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
encrypt_button = tk.Button(text="Save & Encrypt",font="Arial 10 normal",command=save_encrypt)
decrypt_button = tk.Button(text="Decrypt",font="Arial 10 normal",command=decrypt_command)
encrypt_button.pack(pady=5)
decrypt_button.pack()


tk.mainloop()