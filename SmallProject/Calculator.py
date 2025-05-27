from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def click(num):
    global VarText
    VarText += str(num)
    equation.set(VarText)
    
def key_click(event):
    char = event.char
    if char in '0123456789+-*/.':
        click(char)
    elif event.keysym in ("Return", "equal"):
        equal()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

def equal(event=None):
    try:
        global VarText
        total = str(eval(VarText))
        equation.set(total)
        VarText = total
    
    except ZeroDivisionError:
        messagebox.showwarning("Error", "You cannot divided by 0!")
        clear()

    except SyntaxError:
        messagebox.showerror("Error", "Syntax Error!")
        clear()

    except Exception:
        messagebox.showerror("Error", "Something gone wrong")
        clear()

def clear(event=None):
    global VarText
    equation.set("")
    VarText = ""

def backspace():
    global VarText
    VarText = VarText[:-1]
    equation.set(VarText)

window = Tk()
window.title('Calculator')
window.resizable(0,0)
icon = PhotoImage(file="G:\\My Drive\\Projects\\Python\\General\\Attachments\\calculator.png")
window.iconphoto(True,icon)

equation = StringVar()
VarText = ""
frame = Frame(window,bd=5,relief=SUNKEN,background='black')
frame.pack()
display = Entry(frame, textvariable=equation, font=("Cambria", 30),bg='black',fg='white',width=13)
display.grid(row=0, column=0, columnspan=4,ipadx=8, ipady=12)
display.config(xscrollcommand=lambda *args: None)


button = [
    (1, 1, 0), (2, 1, 1), (3, 1 ,2), ("+", 1, 3),
    (4, 2, 0), (5, 2, 1), (6, 2, 2), ("-", 2, 3),
    (7, 3, 0), (8, 3, 1), (9, 3, 2), ("*", 3, 3),
    (0, 4, 0), (".", 4, 1), ("/", 4, 3)
    ]

for txt, r, c in button:
    Button(frame,text=txt,font=("Cambria",30),bg='#111111',fg='white',activebackground='lightgrey',activeforeground='white',width=3, command= lambda t = txt: click(t)).grid(row=r,column=c)

Button(frame, text="=", font=("Cambria",30), width=3,bg='#111111',fg='white',activebackground='lightgrey',activeforeground='white', command=equal).grid(row=4, column=2)
Button(frame, text="Clear", font=("Cambria", 22), width=9,bg='#111111',fg='white', activebackground='lightgrey',activeforeground='white', command=clear).grid(row=5, column=0, columnspan=2)
Button(frame, text="BackSpace", font=("Cambria", 22), width=9,bg='#111111',fg='white', activebackground='lightgrey',activeforeground='white', command=backspace).grid(row=5, column=2, columnspan=2)


window.bind("<Key>", key_click)
window.bind("<Return>", equal)
window.bind("<equal>", equal)
window.bind("<BackSpace>", lambda e: backspace())

window.mainloop()