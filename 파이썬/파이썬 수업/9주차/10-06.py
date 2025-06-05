from tkinter import *
from tkinter import messagebox

def myFuc() :
        messagebox.showinfo("심슨 버튼", "심슨이 귀엽죠?")
    
window = Tk()

photo = PhotoImage(file = "C:\\Users\\titic\\OneDrive\\바탕 화면\\파이썬\\a.gif")
button1 = Button(window, image = photo, command = myFuc)

button1.pack()

window.mainloop()