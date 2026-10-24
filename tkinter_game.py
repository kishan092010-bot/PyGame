import tkinter     
from datetime import date

# Creates a TKinter Window
root = tkinter.Tk()

# Sets a title
root.title("Getting Started with Widgets")

# 
root.geometry("400x300")

lbl = Label(text = "Hey There!", fg = "white", bg = "#072F5F", height = 1, width = 300)

name_lbl = Label(text = "Full Name", bg = "#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the Application \n & Today's date is: "
    greet = "Hello" + name + "\n"
    text_box = Text(height = 3)
