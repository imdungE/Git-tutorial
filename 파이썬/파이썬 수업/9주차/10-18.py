from tkinter import *
from tkinter import messagebox

def func_open() : 
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")
    
def func_exit() :
    window.quit()
    window.destroy()
    
window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

filemenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = filemenu)
filemenu.add_command(label = "열기", command = func_open)
filemenu.add_separator()
filemenu.add_command(label = "종료", command = func_exit)

window.mainloop()