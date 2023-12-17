from tkinter import *

def BaseWindow():
    window = Tk()
    window.title("AppLauncher")
    window.configure(width=500, height=300)
    window.configure(bg='lightgray')
    window.eval('tk::PlaceWindow . center')
    window.mainloop()

BaseWindow()