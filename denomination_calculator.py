from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Student Management System")
root.configure(bg = "light blue")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top, text = "this is top level window")
    l2.pack()
    top.mainloop() 

l = Label(root, text = "Welcome to Student Management System!")
btn = Button(root,
             text = "click here to open another window",
             command = topwin)

l.pack()
btn.pack()

root.mainloop()


# Task 1
    # 1. Change the main window title to studnet management system
    # 2. Set the window size to 500 x 500
    # 3. Change the background color to light blue
    # 4. Add a label displaying welcome to studnet management system

# Task 2
    # Create a button named "Add Student"
    # When the user clicks the button open a new top level window
    # Set its title to student details
    # Display the message & enter student's information


def student_details_window():
    global new_win
    new_win = Toplevel()
    new_win.title("Student details")

btn1 = Button(master = root, text = "Add Student", command = student_details_window)
btn1.pack()

