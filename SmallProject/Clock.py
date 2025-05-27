from tkinter import *
from time import *

# function for updating the clock
def update():
    clock = strftime("%H:%M:%S")
    label_clock.config(text=clock)

    calendar = strftime("%a %d %b %Y")
    label_date.config(text=calendar)

    window.after(1000, time)

window = Tk()

# Icon and Title
window.title('Clock')
clock_icon = PhotoImage(file="G:\\My Drive\\Projects\\Python\\General\\Attachments\\clock.png")
window.iconphoto(True,clock_icon)
window.config(background="black")

# Label for displaying date and time
label_clock = Label(window, font=("Futura",48),background='black',foreground='lime')
label_date = Label(window, font=("Futura",20),background='black',foreground='white')

label_clock.pack()
label_date.pack()
update()

window.mainloop()
