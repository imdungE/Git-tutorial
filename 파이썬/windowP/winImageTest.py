from tkinter import *
window = Tk()

photo = PhotoImage(file = "C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\파이썬\\windowP\\KakaoTalk_20250510_235513769.jpg")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()