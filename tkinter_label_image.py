from tkinter import *

root = Tk()
root.geometry ("300x200")

photo = PhotoImage(file="dog.png")
label = Label(root, image = photo)
label.pack()

root.mainloop()