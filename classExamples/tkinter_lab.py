print("tkinter example")

from tkinter import *

window = Tk()
window.title("class example")

canvas = Canvas(window, width = 400, height = 500)
canvas.pack()

window.mainloop(30)


canvas.create_oval(175, 25, 225, 75) #head
canvas.create_line(200,75,200,200)
canvas.create_line(200,100,250,70)
canvas.create_line(200,100,170,150)
canvas.create_line(200,200,180,250)
canvas.create_line(200,200,220,250)