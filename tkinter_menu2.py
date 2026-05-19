from tkinter import *

wnd = Tk()
wnd.title("shinyeonho")
wnd.geometry("600x400")
wnd.resizable(False,False)

def close():
    wnd.quit()
    wnd.geometry()

def p_fri(a, b):
    print(a)
    print(b)

def p_fri2():
    print('leeemonade!')

def p_fri3():
    print(f'value1: {value1.get()} | value2: {value2.get()} | value3: {value3.get()} | value4: {value4.get()}')


menubar = Menu(wnd)

fkqpf = Label(wnd)

label1 = Label(wnd, text='this is label1')
label1.pack

filemenu = Menu(menubar, tearoff=0, tearoffcommand=p_fri, postcommand=p_fri2)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="print", command=p_fri3)
filemenu.add_command(label="quit", command=close)
# menumenu = Menu(filemenu)
# menumenu.add_cascade(label="more menu", menu=filemenu)
# filemenu.add_command(label="lemon1")
# filemenu.add_command(label="lemon2")
wnd.config(menu=menubar)

value1 = IntVar()
button1 = Checkbutton(wnd, text="Python", variable=value1)
button1.pack(side='left')
value2 = IntVar()
button2 = Checkbutton(wnd, text="Java", variable=value2)
button2.pack(side='left')
value3 = IntVar()
button3 = Checkbutton(wnd, text="Clang", variable=value3)
button3.pack(side='left')
value4 = IntVar()
button4 = Checkbutton(wnd, text="Swift", variable=value4)
button4.pack(side='left')



wnd.mainloop()