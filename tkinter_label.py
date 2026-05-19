from tkinter import *

root = Tk()
root.geometry ("300x200")
click_count = 0

def button_clicked(): ##콜백함수
    global click_count
    print("Button is Clicked")
    click_count += 1
    label.config(text=click_count)
    

label = Label(root, text = click_count)
# label1 = Label(root, text = "123")
# label1.pack()
label.pack()

button = Button(root, text = "Click", command = button_clicked)
button.pack()

root.mainloop()