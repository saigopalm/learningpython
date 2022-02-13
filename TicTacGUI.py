from tkinter import *

win = Tk()
win.title("Tic Tac Toe")
win.geometry('600x666+600+150')
#win.resizable(False, False)

bg = PhotoImage(file = 'bg.png')

canvas = Canvas(win, width= 700, height=700)
canvas.pack(fill = "both", expand = True)
canvas.create_image(0,0, image=bg, anchor= "nw")

#button1 = Button(canvas, background= '#231840', height = 12, width = 20, borderwidth=0)
#button1.place(x = 0, y = 0)

win.mainloop()