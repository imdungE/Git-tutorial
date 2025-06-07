from tkinter import *

window = None

canvas = None 
XSIZE, YSIZE = 256, 256

window = Tk()
canvas = Canvas(window, height = XSIZE, width = YSIZE)
# +RAW이미지 출력 코드 
paper = PhotoImage(width = XSIZE, height = YSIZE)
paper.put("red", to = (0, 0, XSIZE, YSIZE))
canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = "normal")

canvas.pack()
window.mainloop()