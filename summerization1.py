import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

import os

root = tk.Tk()
root.geometry("1920x780")
root.title("Text Summerizer and Sentiment Analysis")
root.configure(bg="#83a1c5")

#def selected():
    #myLabel = Label(root).pack()


#options = [
 #   "Method1",
  #  "Method2",
   # "Method3",
#]

#clicked = StringVar()
#clicked.set(options[0])

#drop = OptionMenu(root, clicked, *options)
#drop.pack()

#myButton = Button(root, text="select from list", command=selected)
#myButton.pack(pady=50)

myLabel = Label(root, text="Input")
myLabel.pack(side=LEFT)

t = Text(root, height=20, width=40, borderwidth=5)
t.pack(side=LEFT)

myLabel = Label(root, text="Summary",)
myLabel.pack(side=RIGHT)
r = Text(root, height=20, width=40, borderwidth=5)
r.pack(side=RIGHT)

p = Text(root, height=20, width=40, borderwidth=5,)
p.pack()

frame = Frame(root)
frame.pack(fill=BOTH)

combobox = Combobox(frame)
items = ("Method1","Method2", "Method3")
combobox['values'] = items
combobox.current(0)

combobox.pack(side=LEFT)

root.mainloop()

