from tkinter import *

btnList = [None] * 9
fnameList = ["a.gif", "b.gif", "c.gif", "d.gif", "e.gif", "f.gif", "g.gif", "h.gif", "i.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("210x210")

for i in range(0, 9) : 
    photoList[i] = PhotoImage(file = "C:\\Users\\titic\\OneDrive\\바탕 화면\\파이썬\\" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])
    
for i in range(0, 3) : 
    for k in range(0, 3) : 
        btnList[num].place(x = xPos, y = yPos)
        xPos += 70
        num += 1
    xPos = 0
    yPos += 70
    
window.mainloop()