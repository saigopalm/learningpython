from tkinter import * # importing the tkinter module
from tkinter import messagebox

win = Tk() # creating a window
win.title('SG Calculators')
win.geometry('600x400+800+200')
win.configure(bg='#00E563')
win.resizable(False, False)

l = Label(win, text = "CONVERT A DECIMAL NUMBER INTO BINARY", bg = '#00E563')
l.config(font=("Courier",15, "bold"))
l.place(relx = 0.15, rely = 0)

l1 = Label(win, text = "Enter a decimal number", bg = '#00E563')
l1.config(font=("Courier",15, "bold"))
l1.place(relx = 0.001, rely = 0.18)

entry = Entry(win, width = 10, bg = '#FFFFC4', font=("Courier New",15))
entry.place(relx = 0.15, rely = 0.3)

menu = StringVar()
menu.set("Convert to")

w = OptionMenu(win , menu , "Binary", "Ternary", "Octal", "Hexadecimal")
w.config(bg = "#bb4244", fg = "WHITE")
w["menu"].config(bg="#ff9200")
w.place(relx = 0.76, rely = 0.18)

l2 = Label(win,bg = '#00E563')

def convert():
    l2.config(text = "")
    x = int(entry.get())
    if x > 9999999999: 
        messagebox.showerror('Error', 'Entered number is too big to handle')
        return
    if x < 0 :
         messagebox.showerror('Error', 'Enter a positive integer')
    binary = str('')
    while(x > 0):
        binary = str(x % 2) + binary
        x = x // 2
    
    l2.config(text = "In Binary:: " + binary)
    l2.config(font=("Courier",15, "bold"))
    l2.place(relx = 0.001, rely = 0.5)
    

l3 = Label(win, text = "              Created in Gopal Labs                     ", bg = '#255248', fg='white')
l3.config(font=("Courier",15, "bold"))
l3.place(relx = 0, rely = 0.9)

button = Button(win, text = 'Convert', height = 4, width = 5, command = convert, bg= '#001662', fg='white')
button.config(font=("Courier",15, "bold"))
button.place(relx = 0.5, rely = 0.16)

win.mainloop()
