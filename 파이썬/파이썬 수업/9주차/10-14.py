from tkinter import *
from tkinter import messagebox

def clickImage(event) : 
    messagebox.showinfo("마우스", "심슨에서 마우스가 클릭됨")
    
window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "C:\\Users\\titic\\OneDrive\\바탕 화면\\파이썬\\a.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()