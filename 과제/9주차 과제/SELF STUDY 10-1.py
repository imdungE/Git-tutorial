from tkinter import *
window = Tk()

photo = PhotoImage(file = "C:\\Users\\titic\\OneDrive\\바탕 화면\\파이썬\\a.gif")
photo2 = PhotoImage(file = "C:\\Users\\titic\\OneDrive\\바탕 화면\\파이썬\\b.gif")
label1 = Label(window, image = photo)
label2 = Label(window, image = photo2)

label1.pack(side = LEFT)
label2.pack(side = RIGHT)

window.mainloop()