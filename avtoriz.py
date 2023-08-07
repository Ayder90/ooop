lst = []

import random
from tkinter import *
import pyodbc
import tkinter
from tkinter import messagebox
from tkinter import ttk

# class Users:
#     def __init__(self, name, surname, login, password, mail, info):
#         self.name = name
#         self.surname = surname
#         self.login = login
#         self.password = password
#         self.mail = mail
#         self.info = info
#     def your_info(self):
#         print(self.name, self.surname, self.info)
# def register():
#     u_name = input("Введите имя: ")
#     u_surname = input("Введите фамилию: ")
#     u_login = input("Введите логин: ")
#     u_password = input("Введите пароль: ")
#     u_mail = input("Введите mail: ")
#     u_info = input("Расскажите о себе: ")
#     user = Users(u_name, u_surname, u_login, u_password, u_mail, u_info)
#     lst.append(user)


connection = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost\sqlexpress;DATABASE=Users;Trusted_Connection=Yes") # Соединение с базой данных

kyrsor = connection.cursor()

# kyrsor.execute("SELECT * FROM User_baza")
# all = kyrsor.fetchall()
# for user_in_all in all:
#     print(user_in_all.Email)



def register():
    reg_name = entry_name.get().strip()
    reg_surname = entry_surname.get().strip()
    reg_login = entry_login1.get().strip()
    reg_password = entry_password1.get().strip()
    reg_email = entry_email.get()
    reg_info = entry_info.get()
    if reg_name != "" and reg_surname != "" and reg_login != "" and reg_password != "":
        kyrsor.execute(f"INSERT INTO User_baza VALUES('{reg_name}','{reg_surname}','{reg_login}','{reg_password}','{reg_email}','{reg_info}')")
        tkinter.messagebox.showinfo(title="Успешная регистрация", message = "Добро пожаловать в программу")
        connection.commit()
        entry_name.delete(0, END)
        entry_surname.delete(0, END)
        entry_login1.delete(0, END)
        entry_password1.delete(0, END)
        entry_email.delete(0, END)
        entry_info.delete(0, END)
        label_yved_0.config(text="")
        label_yved_1.config(text="")
        label_yved_2.config(text="")
        label_yved_3.config(text="")
    else:
        if reg_name == "":
            label_yved_0.config(text="Не заполненное поле")
        else:
            label_yved_0.config(text="")

        if reg_surname == "":
            label_yved_1.config(text="Не заполненное поле")
        else:
            label_yved_1.config(text="")

        if reg_login == "":
            label_yved_2.config(text="Не заполненное поле")
        else:
             label_yved_2.config(text="")

        if reg_password == "":
            label_yved_3.config(text="Не заполненное поле")
        else:
             label_yved_3.config(text="")

    

def avtoriz():
    Flag = False
    u_login1 = entry_login.get()
    u_password1 = entry_password.get()
    kyrsor.execute("SELECT Login, Password, Info FROM User_baza")
    dan = kyrsor.fetchall()
    for login_pass in dan:
        if u_login1 == login_pass.Login:
            Flag = True
            if u_password1 == login_pass.Password:
                tkinter.messagebox.showinfo(title="Успешная авторизация", message = f"Добро пожаловать в программу\nИнформация о пользователе:{login_pass.Info} ")
                break
            else:
                tkinter.messagebox.showerror(title="Ошибка", message = "Пароль введен неправильно")     
    if Flag == False:
        tkinter.messagebox.showerror(title="Ошибка", message = "Пользователь не найден") 
    entry_login.delete(0, END)
    entry_password.delete(0, END)


# def generator():
#     a = "0123456789"
#     b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     c = "abcdefghijklmnopqrstuvwxyz"
#     d = "!№;%::?*()"
#     bykva = a + b + c + d
#     str = ""
#     result = str.join(random.sample(bykva, 5))
#     print(result)

# print("Добро пожаловать!")



window = Tk()

window.title("Регистрация")
window.geometry("700x500")

per = ttk.Notebook(window)

frame_reg = ttk.Frame(per)
frame_login = ttk.Frame(per)
per.add(frame_login, text="Авторизация")
per.add(frame_reg, text="Регистрация")

# Вкладка авторизации
label = Label(frame_login, text="Логин: ")
label.config(font=("Times New Roman", 24))
label2 = Label(frame_login,text="Пароль: ")
label2.config(font=("Times New Roman", 24))

entry_login = Entry(frame_login)
entry_password = Entry(frame_login)
btn = Button(frame_login, text="Вход", width=17, command=avtoriz)


# btn.grid()
# btn2.grid()

label.place(x=100, y = 100)
entry_login.place(x=200, y= 115)
label2.place(x=75, y=135)
entry_password.place(x=200, y=150)
btn.place(x=200, y=175)


# Вкладка регистрации
label_yved_0 = Label(frame_reg, text=" ", fg="red")
label_yved_0.config(font=("Times New Roman", 13))
label_yved_0.place(x=370, y=55)
label_yved_1 = Label(frame_reg, text=" ", fg="red")
label_yved_1.config(font=("Times New Roman", 13))
label_yved_1.place(x=370, y=80)
label_yved_2 = Label(frame_reg, text=" ", fg="red")
label_yved_2.config(font=("Times New Roman", 13))
label_yved_2.place(x=370, y=105)
label_yved_3 = Label(frame_reg, text=" ", fg="red")
label_yved_3.config(font=("Times New Roman", 13))
label_yved_3.place(x=370, y=130)


label_name = Label(frame_reg, text="Имя", width=10, anchor="e")
label_name.config(font=("Times New Roman", 17))
label_surname = Label(frame_reg, text="Фамилия", width=10, anchor="e")
label_surname.config(font=("Times New Roman", 17))
label_login = Label(frame_reg, text="Логин", width=10, anchor="e")
label_login.config(font=("Times New Roman", 17))
label_password = Label(frame_reg, text="Пароль", width=10, anchor="e")
label_password.config(font=("Times New Roman", 17))
label_email = Label(frame_reg, text="Email", width=10, anchor="e")
label_email.config(font=("Times New Roman", 17))
label_info = Label(frame_reg, text="Информация", width=10, anchor="e")
label_info.config(font=("Times New Roman", 17))

entry_name = Entry(frame_reg)
entry_name.config(font=("Times New Roman", 10))
entry_name.delete(1, END)
entry_surname = Entry(frame_reg)
entry_surname.config(font=("Times New Roman", 10))
entry_login1 = Entry(frame_reg)
entry_login1.config(font=("Times New Roman", 10))
entry_password1 = Entry(frame_reg)
entry_password1.config(font=("Times New Roman", 10))
entry_email = Entry(frame_reg)
entry_email.config(font=("Times New Roman", 10))
entry_info = Entry(frame_reg)
entry_info.config(font=("Times New Roman", 10))



label_name.place(x=100, y=50)
entry_name.place(x=245, y=56)

label_surname.place(x=100, y=75)
entry_surname.place(x=245, y=81)

label_login.place(x=100, y=100)
entry_login1.place(x=245, y=106)

label_password.place(x=100, y=125)
entry_password1.place(x=245, y=131)

label_email.place(x=100, y=150)
entry_email.place(x=245, y=156)

label_info.place(x=100, y=175)
entry_info.place(x=245, y=181)

btn2 = Button(frame_reg, text="Зарегестрироваться", width=17, command=register)
btn2.place(x=240, y=210)

per.pack(expand=1, fill="both")


window.mainloop()


