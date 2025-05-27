import os
from tkinter import *
from tkinter import filedialog, colorchooser, font, ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def main():
    def fontColors():
        color = colorchooser.askcolor(title = "Pick a font color")
        text.config(fg=color[1])

    def fontFamilies(event = None):
        text.config(font=(font_name.get(), size_box.get()))

    def bgColors():
        color = colorchooser.askcolor(title = "Change color theme")
        text.config(bg=color[1])

    def createTab():
        pass

    def newFile():
        window.title("Untitled")
        text.delete(1.0, END)

    def openFile():
        file = askopenfile(
            defaultextension = ".txt",
            filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
        
        if file:
            try:
                window.title(os.path.basename(file.name))
                text.delete(1.0, END)
                text.insert(1.0, file.read())

            except Exception:
                print("Couldn't read file")
                
            finally:
                file.close()

    def saveFile(event = None):
        file = filedialog.asksaveasfile(
            initialfile = 'untitled.txt',
            defaultextension = ".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        
        if file:
            try:
                window.title(os.path.basename(file.name))
                file.write(text.get(1.0, END))

            except Exception:
                print("Couldn't save file")
            
            finally:
                file.close()

    def cut():
        text.event_generate("<<Cut>>")

    def copy():
        text.event_generate("<<Copy>>")

    def paste():
        text.event_generate("<<Paste>>")

    def quit():
        window.destroy()

    window = Tk()
    window.title("NvPad")
    icon = PhotoImage(file="G:\\My Drive\\Projects\\Python\\General\\Attachments\\neovim.png")
    window.iconphoto(True,icon)
    file = None

    # Window size and placement
    window_width = 640
    window_height = 640
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

    # Font
    font_name = StringVar(window)
    font_name.set("Consolas")

    font_size = StringVar(window)
    font_size.set("11")

    text = Text(font = (font_name.get(), font_size.get()))

    # Text Area
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    text.grid(sticky=N + E + S + W)

    # Scrollbar
    scrollbar = Scrollbar(text)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.config(yscrollcommand=scrollbar.set)

    # Ribbon menu
    frame = Frame(window)
    frame.grid()

    # Font Color
    color_button = Button(frame, text = "Color", command = fontColors)
    color_button.grid(row = 0, column = 0)

    # Font Family
    font_families = ttk.Combobox(frame, textvariable = font_name, values = [*font.families()])
    font_families.grid(row = 0, column = 1)
    font_families.bind("<<ComboboxSelected>>", fontFamilies)

    size_box = Spinbox(frame, from_ = 1, to = 100, textvariable = font_size, command = fontFamilies)
    size_box.grid(row = 0, column = 2)

    # Background Color
    bg_color = Button(frame, text = "Theme", command = bgColors)
    bg_color.grid(row = 0, column = 3)

    # Menu Bar
    menu_bar = Menu(window)
    window.config(menu = menu_bar)

    # File menu
    file_menu = Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(label = "File", menu = file_menu)
    file_menu.add_command(label = "New", command = newFile)
    file_menu.add_command(label = "Open", command = openFile)
    file_menu.add_command(label = "Save", command = saveFile)
    file_menu.add_separator()
    file_menu.add_command(label = "Exit", command = quit)

    # Edit menu
    edit_menu = Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(label = "Edit", menu = edit_menu)
    edit_menu.add_command(label = "Cut", command = cut)
    edit_menu.add_command(label = "Copy", command = copy)
    edit_menu.add_command(label = "Paste", command = paste)

    # Key Binding
    window.bind("<Control-s>", lambda e: saveFile())
    window.bind("<Control-n>", lambda e: newFile())
    window.bind("<Control-o>", lambda e: openFile())

    window.mainloop()

if __name__ == '__main__':
    main()
