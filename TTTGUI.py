from tkinter import *

win = Tk()
win.title("Tic Tac Toe")
win.geometry('560x553+600+150')
win.resizable(False, False)

button1 = Button(win, background= '#231840', width = 15, height = 10)
button1.grid(row=0, column=0)

button2 = Button(win, background= '#231840', width = 15, height = 10)
button2.grid(row=0, column=1)

button3 = Button(win, background= '#231840', width = 15, height = 10)
button3.grid(row=0, column=2)

button4 = Button(win, background= '#231840', width = 15, height = 10)
button4.grid(row=1, column=0)

button5 = Button(win, background= '#231840', width = 15, height = 10)
button5.grid(row=1, column=1)

button6 = Button(win, background= '#231840', width = 15, height = 10)
button6.grid(row=1, column=2)

button7 = Button(win, background= '#231840', width = 15, height = 10)
button7.grid(row=2, column=0)

button8 = Button(win, background= '#231840', width = 15, height = 10)
button8.grid(row=2, column=1)

button9 = Button(win, background= '#231840', width = 15, height = 10)
button9.grid(row=2, column=2)

reset = Button(win, text="Reset", fg= 'white', background= 'red', width=10, height = 3)
reset.grid(row=1, column=4)

win.mainloop()