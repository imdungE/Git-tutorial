from tkinter import *
from tkinter import messagebox

def keyEvent(event) : 
    if event.keysym == "Up" :
        messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 위쪽 화살표")
    elif event.keysym == "Down" :
        messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 아래쪽 화살표")
    elif event.keysym == "Left" :
        messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 왼쪽 화살표")
    elif event.keysym == "Right" :
        messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 오른쪽 화살표")


window = Tk()

window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Down>", keyEvent)
window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Right>", keyEvent)

window.mainloop()
