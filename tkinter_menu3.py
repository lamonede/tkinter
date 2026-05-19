from tkinter import *

wnd = Tk()
wnd.title("Double Cascade Example")
wnd.geometry("400x300")

# 1. 최상위 메뉴바 생성
menubar = Menu(wnd)

# 2. 첫 번째 레벨: File 메뉴 생성
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

# 3. 두 번째 레벨: Recent Files 하위 메뉴 생성 (부모를 file_menu로 지정)
recent_menu = Menu(file_menu, tearoff=0)
recent_menu.add_command(label="Project_01.py")
recent_menu.add_command(label="Project_02.py")

# 4. File 메뉴에 하위 메뉴(recent_menu)를 Cascade로 연결
file_menu.add_cascade(label="Open Recent", menu=recent_menu)

# 5. 기타 일반 명령 추가
file_menu.add_separator() # 구분선
file_menu.add_command(label="Exit", command=wnd.quit)

# 윈도우에 메뉴바 등록
wnd.config(menu=menubar)
wnd.mainloop()