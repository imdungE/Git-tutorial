from tkinter import *
window = Tk()

photo = PhotoImage(file = "C:\\Users\\titic\\OneDrive\\바탕 화면\\파이썬\\a.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()