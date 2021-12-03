from tkinter import *

window = Tk()
window.title("GUI window")
window.minsize(width=500, height=300)


mylabel = Label(text="Enter mile ")
mylabel.grid(column=0, row=0)


inputuser = Entry()

inputuser.grid(column=5, row=0)


def click():
    """
convert miles  to km
    """
    mile = float(inputuser.get())
    km=mile*1.68
    mylabel1.config(text=f"Output in km {km}")


button = Button(text='convert', command=click)

button.grid(column=10, row=0)


mylabel1 = Label(text="Output in km ")

mylabel1.grid(column=0, row=10)

window.mainloop()