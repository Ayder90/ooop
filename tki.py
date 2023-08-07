from tkinter import *
from tkinter import ttk

counter = 0
def change_label():
    global counter
    counter += 1
    label["text"] = counter

window = Tk() 

window.title("Grand Theft Auto")
window.geometry("300x400")
#window.resizable(False, False)
window.minsize(100,150)


label = Label(text="Всем привет!")
label.pack(anchor="w")

button1 = ttk.Button(text="Зеленый", command=change_label)
button1.pack(anchor="w")
button2 = Button(text="Синий")
button2.pack(fill=X)



window.mainloop()


