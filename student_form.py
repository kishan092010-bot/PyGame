import tkinter

root = tkinter.Tk()
root.title("Login App") # Title
root.geometry("400,400")

# Placed inside the widnow - Frame
frame = Frame(master = root, height = 200, width = 360, bg = "#d0efff")

# fg = Text Color & Label inside the Frame
lbl1 = Label(frame, text = "Full Name", bg = "#3895D3", fg = "white", width = 12)
lbl2 = Label(frame, text="Email ID", bg="#3895D3", fg="white", width=12)
lbl3 = Label(frame, text="Enter Password", bg="#3895D3", fg="white", width=12)

# Create the Entry Widget (a box where a user can create a single type of text)
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show = "*")

# Create a function that displays a message
def display():
    
