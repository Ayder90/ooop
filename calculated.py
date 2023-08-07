from tkinter import *
from tkinter import ttk


window = Tk()

label = Label(text="Введите пример нажимая на кнопки снизу:")
label.pack(fill="x")



window.title("Calculated")
window.geometry("500x600")

txt = Entry(window, width=10)
txt.pack(side="top")


def ent(button):
    text = button.cget("text")
    text_entry = txt.get()
    txt.delete(0, END)
    txt.insert(0, text_entry + text)

def ravno():
    result = eval(txt.get())
    txt.delete(0, END)
    txt.insert(0, result)


a = Label(text="Выберите число:")
a.pack(fill="x")

button1 = Button(window, text="0", command = lambda: ent(button1))
button1.pack(fill="x")
button2 = Button(window, text="1", command=lambda: ent(button2))
button2.pack(fill="x")
button3 = Button(window, text="2", command=lambda: ent(button3))
button3.pack(fill="x")
button4 = Button(window, text="3",command=lambda: ent(button4))
button4.pack(fill="x")
button5 = Button(window, text="4",command=lambda: ent(button5))
button5.pack(fill="x")
button6 = Button(window, text="5", command=lambda: ent(button6))
button6.pack(fill="x")
button7 = Button(window, text="6", command=lambda: ent(button7))
button7.pack(fill="x")
button8 = Button(window, text="7", command=lambda: ent(button8))
button8.pack(fill="x")
button9 = Button(window, text="8", command=lambda: ent(button9))
button9.pack(fill="x")
button10 = Button(window, text="9", command=lambda: ent(button10))
button10.pack(fill="x")

b = Label(text="Выберите действие:")
b.pack(fill="x")

button11 = Button(window, text="+",command=lambda: ent(button11))
button11.pack(fill="x")
button12 = Button(window, text="=", command = ravno)
button12.pack(fill="x")

window.mainloop()