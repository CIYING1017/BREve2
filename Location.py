from tkinter import *
from tkinter.font import BOLD, Font
from tkinter.ttk import Label

root = Tk()

# creating title widget
myLabel1 = Label (root, text = "Location info")
myLabel2 = Label (root, text = "Put in coordinates or postcodes to obtain terrain and topographic data")

# create entry widget
# e = Entry (root, width = 50, borderwidth = 5)
# e.pack()


# define a function where when you click ,it responses with a sentence
# def myClick():
#     myLabel3 = Label (root, text ="Hello "+e.get())
#     myLabel3.pack()


root.bold25 = Font (root.master, size = 100, weight = BOLD)

# myButton = Button  (root, text = "Enter your name", padx=50,pady=10, command = myClick, fg="blue", bg = "white")


# shoving it onto the screen
# myLabel1.pack()
myLabel1.grid (row=0, column=0)
# myButton.pack()


myLabel2.grid (row=1, column=0)
# myButton.grid(row=2, column=0)


root.mainloop()

