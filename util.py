import tkinter as tk
from tkinter import messagebox

def get_button(window, text, color, command, fg='white', relief='raised', borderwidth=2, font=('Helvetica', 16, 'bold')):
    button = tk.Button(
        window,
        text=text,
        activebackground="black",
        activeforeground="white",
        fg=fg,
        bg=color,
        command=command,
        height=2,
        width=20,
        font=font,
        relief=relief,
        borderwidth=borderwidth,
        cursor="hand2"
    )
    return button

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label(window, text, font=('Helvetica', 18, 'bold'), fg='black'):
    label = tk.Label(window, text=text, fg=fg, font=font, justify="left")
    return label

def get_entry_text(window, height=1, width=30, font=("Arial", 16)):
    inputtxt = tk.Text(window, height=height, width=width, font=font)
    return inputtxt

def msg_box(title, description):
    messagebox.showinfo(title, description)
