from tkinter import *

# def get_osoe_value():
#     value = osoe.get()
#     print("Entered value:", value)

root = Tk()
root.title("leemonade")
root.geometry("640x480+100+100")
root.resizable(False, False)

def close():
    root.quit()
    root.geometry()

def conslog():
    print("lemonade")

menubar = Menu(root)

menu_1 = Menu(menubar, tearoff=0)
menu_1.add_command(label="하위 메뉴 1-1")
menu_1.add_command(label="하위 메뉴 1-2")
menu_1.add_separator()
menu_1.add_command(label="종료", command=close)
menubar.add_cascade(label="메뉴", menu=menu_1)

root.config(menu=menubar)

root.mainloop()