from operator import itemgetter
from typing import ItemsView
import flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from datetime import datetime
import pandas
import pyodbc
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import requests

# from sqlalchemy_imageattach.entity import Image, image_attachment
server = "localhost\sqlexpress"
date_base = "Avtozvyk"
driver = "ODBC Driver 17 for SQL Server"
db_connection = f"mssql://@{server}/{date_base}?driver={driver}"
engine = create_engine(db_connection) # Создание движка базы данных
connection_engine = engine.connect()
pyodbc_connection = pyodbc.connect(r"Driver=SQL Server;Server=.\SQLEXPRESS;Database=Avtozvyk;Trusted_Connection=yes;")
cursor = pyodbc_connection.cursor()
zapros = pandas.read_sql_query("SELECT * FROM Ysiliteli", connection_engine) # позволяет считывать запрос sql
print(zapros)
f = Flask(__name__)
# f.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Avtozvyk.db" 
f.config["SQLALCHEMY_DATABASE_URI"] = f"mssql://@{server}/{date_base}?driver={driver}" # Подключение и соединение с движком базы данных
db = SQLAlchemy(f)


with f.app_context():
    # db.create_all()
    pass


@f.route("/")
def glav():
    return render_template("flask.html")

@f.route("/about", methods = ["POST", "GET"])
def kop():
    if request.method == "POST":
        name = request.form["firstName"]
        surname = request.form["lastName"]
        email = request.form["email"]
        address = request.form["address"]
        nomer = request.form["username"]
        k = db.USERS(Name_user = name, Surname = surname, Nomer = nomer, Email = email, Address = address)
        # try:
        db.session.add(k)
        db.session.commit()
        return redirect("/zakaz")
        # except:
        # return "При заполнении записи произошла ошибка"
    else:
        return render_template("flask2.html")



@f.route("/zakaz")
def zak():
    # p = db.USERS.query.order_by(db.USERS.id).all()
    cursor.execute("SELECT * FROM USERS")
    p = cursor.fetchall()
    return render_template("zak.html", p = p) # p - то как мы будем обращаться к нашим заказам

@f.route("/ayder", methods = ["POST", "GET"])
def lop():
    if request.method == "POST":
        Email = request.form["email"]
        Password = request.form["password"]
        print(Email, Password)
        cursor.execute("SELECT Email, Password, Id FROM USERS")
        r = cursor.fetchall()
        print(r)
        Flag = False
        for i in r:
            if i[0] == Email:
                if i[1] == Password:
                    print("Успешная авторизация")
                    return redirect("/")
                else:
                    Flag = True
                    print("Пароль не верный")
            else:
                Flag = True
        if Flag == True:
            return render_template("Avtorizacia.html", flag = Flag)    
    else:
        return render_template("Avtorizacia.html", flag = False)

@f.route("/user/<string:name>/<int:id>")
def user(name, id):
    return name+str(id)

@f.route("/flask2")
def ali():
    return render_template("flask2.html")

@f.route("/maket")
def aloo():
    return render_template("maket.html")



@f.route("/Oval1", methods = ["POST", "GET"])
def Oval1():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Dinamik_OVAL.id, Производитель, Модель, Цена, Image FROM Dinamik_Oval WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 1
        link = "/Oval2"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link, type = "Oval")
    else:
        cursor.execute("SELECT Dinamik_OVAL.id, Производитель, Модель, Цена, Image FROM Dinamik_OVAL WHERE Dinamik_OVAL.id < 16 ")
        r = cursor.fetchall()
        page = 1
        link = "/Oval2"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link, type = "Oval")
    

@f.route("/Oval2", methods = ["POST", "GET"])
def Oval2():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Dinamik_OVAL.id, Производитель, Модель, Цена, Image FROM Dinamik_Oval WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 2
        link = "/Oval1"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link, type = "Oval")
    else:
        cursor.execute("SELECT Dinamik_OVAL.id, Производитель, Модель, Цена, Image FROM Dinamik_OVAL WHERE Dinamik_OVAL.id < 16 ")
        r = cursor.fetchall()
        page = 2
        link = "/Oval1"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link, type = "Oval")


@f.route("/dinamik_Twitter1", methods = ["POST", "GET"])
def twit1():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Tvitter_dinamik.id, Производитель, Модель, Цена, Image, Tvitter_dinamik_TYPE.Type_razmer FROM Tvitter_dinamik INNER JOIN Tvitter_dinamik_TYPE ON Tvitter_dinamik_TYPE.id = Tvitter_dinamik.Type_razmer WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 2
        link = "/dinamik_Twitter2"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link, type = "twitter")
    else:
        cursor.execute("SELECT Tvitter_dinamik.id, Производитель, Модель, Цена, Image, Tvitter_dinamik_TYPE.Type_razmer FROM Tvitter_dinamik INNER JOIN Tvitter_dinamik_TYPE ON Tvitter_dinamik_TYPE.id = Tvitter_dinamik.Type_razmer WHERE Tvitter_dinamik.id < 16 ")
        r = cursor.fetchall()
        page = 2
        link = "/dinamik_Twitter2"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link, type = "twitter")
    
@f.route("/dinamik_Twitter2", methods = ["POST", "GET"])
def twit2():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Tvitter_dinamik.id, Производитель, Модель, Цена, Image, Tvitter_dinamik_TYPE.Type_razmer FROM Tvitter_dinamik INNER JOIN Tvitter_dinamik_TYPE ON Tvitter_dinamik_TYPE.id = Tvitter_dinamik.Type_razmer WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 2
        link = "/dinamik_Twitter1"
        return render_template("tovar.htnl", r=r, pag = page, info = "Динамик", link = link, type = "twitter")
    else:
        cursor.execute("SELECT Tvitter_dinamik.id, Производитель, Модель, Цена, Image, Tvitter_dinamik_TYPE.Type_razmer FROM Tvitter_dinamik INNER JOIN Tvitter_dinamik_TYPE ON Tvitter_dinamik_TYPE.id = Tvitter_dinamik.Type_razmer WHERE Tvitter_dinamik.id > 15 and Tvitter_dinamik.id < 31 ")
        r = cursor.fetchall()
        page = 2
        link = "/dinamik_Twitter1"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link, type = "twitter")


@f.route("/dinamik_komponent1", methods = ["POST", "GET"])
def glo():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Dinamik_Komponent.id, Производитель, Модель, Цена, Image, Dinamik_komponent_TYPE.Type_razmer FROM Dinamik_Komponent INNER JOIN Dinamik_komponent_TYPE ON Dinamik_komponent_TYPE.id = Dinamik_Komponent.Type_razmer WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 1
        link = "/dinamik_komponent2"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link,  type = "komponent_dinamik")
        # r = db.USERS.query.order_by(db.USERS.id).all()
    else:
        cursor.execute("SELECT Dinamik_Komponent.id, Производитель, Модель, Цена, Image, Dinamik_komponent_TYPE.Type_razmer FROM Dinamik_Komponent INNER JOIN Dinamik_komponent_TYPE ON Dinamik_komponent_TYPE.id = Dinamik_Komponent.Type_razmer WHERE Dinamik_Komponent.id < 16 ")
        r = cursor.fetchall()
        page = 1
        link = "/dinamik_komponent2"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link,  type = "komponent_dinamik")

@f.route("/dinamik_komponent2", methods = ["POST", "GET"])
def gla():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Dinamik_Komponent.id, Производитель, Модель, Цена, Image, Dinamik_komponent_TYPE.Type_razmer FROM Dinamik_Komponent INNER JOIN Dinamik_komponent_TYPE ON Dinamik_komponent_TYPE.id = Dinamik_Komponent.Type_razmer WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 2
        link = "/dinamik_komponent1"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link,  type = "komponent_dinamik")
    else:    
        # r = db.USERS.query.order_by(db.USERS.id).all()
        cursor.execute("SELECT Dinamik_Komponent.id, Производитель, Модель, Цена, Image, Dinamik_komponent_TYPE.Type_razmer FROM Dinamik_Komponent INNER JOIN Dinamik_komponent_TYPE ON Dinamik_komponent_TYPE.id = Dinamik_Komponent.Type_razmer WHERE Dinamik_Komponent.id > 15 and  Dinamik_Komponent.id < 31  ")
        r = cursor.fetchall()
        page = 2
        link = "/dinamik_komponent1"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик", link = link, type = "komponent_dinamik")

@f.route("/magnitola1", methods = ["POST", "GET"])
def magnitola():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Magnitofon.id, Производитель, Модель, Цена, Image, Type_magnitofon.Type FROM Magnitofon INNER JOIN Type_magnitofon ON Type_magnitofon.id = Magnitofon.Type_magnitofon WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 1
        link = "/magnitola2"
        return render_template("tovar.html", r=r, pag = page,  info = "Магнитола", link = link, type = "magnitola")
        # id = request.form.get('ID')
        # print(id)
    else:
        cursor.execute("SELECT Magnitofon.id, Производитель, Модель, Цена, Image, Type_magnitofon.Type FROM Magnitofon INNER JOIN Type_magnitofon ON Type_magnitofon.id = Magnitofon.Type_magnitofon WHERE Magnitofon.id < 16  ")
        r = cursor.fetchall()
        page = 1
        link = "/magnitola2"
        return render_template("tovar.html", r=r, pag = page,  info = "Магнитола", link = link,  type = "magnitola")

@f.route("/magnitola2", methods = ["POST", "GET"])
def magnitola2():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT  Magnitofon.id, Производитель, Модель, Цена, Image, Type_magnitofon.Type FROM Magnitofon INNER JOIN Type_magnitofon ON Type_magnitofon.id = Magnitofon.Type_magnitofon WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 2
        link = "/magnitola1"
        return render_template("tovar.html", r=r, pag = page, info="Магнитола", link = link, type = "magnitola")
    else:
        cursor.execute("SELECT  Magnitofon.id, Производитель, Модель, Цена, Image, Type_magnitofon.Type FROM Magnitofon INNER JOIN Type_magnitofon ON Type_magnitofon.id = Magnitofon.Type_magnitofon WHERE Magnitofon.id > 15 and Magnitofon.id < 31  ")
        r = cursor.fetchall()
        page = 2
        link = "/magnitola1"
        return render_template("tovar.html", r=r, pag = page,  info = "Магнитола", link = link, type = "magnitola")


@f.route("/dinamik_koaksil1", methods = ["POST", "GET"])
def koaksial_dinamik():
    if request.method == "POST":  
        if "Poisk1" in request.form:
            if request.form["Poisk1"] == "Poisk":
                poisk = request.form["Poisk"].upper()
                print(poisk)
                cursor.execute(f"SELECT Dinamik_Koaksil.id Производитель, Модель, Цена, Image, Razmer_type FROM Dinamik_Koaksil INNER JOIN Types_dinamik_koaksil ON Types_dinamik_koaksil.id = Dinamik_Koaksil.Type_Razmer WHERE Модель LIKE '%{poisk}%' ")
                r = cursor.fetchall()
                page = 1
                link = "/dinamik_koaksil2"
                return render_template("tovar.html", r=r, pag = page, info = "Магнитола", link = link, type = "koaksil_dinamik")
    else:
        cursor.execute("SELECT Dinamik_Koaksil.id, Производитель, Модель, Цена, Image, Razmer_type FROM Dinamik_Koaksil INNER JOIN Types_dinamik_koaksil ON Types_dinamik_koaksil.id = Dinamik_Koaksil.Type_Razmer WHERE Dinamik_Koaksil.id < 16")
        r = cursor.fetchall()
        print(r)
        page = 1
        link = "/dinamik_koaksil2"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик коаксиальный", link = link, type = "koaksil_dinamik")

@f.route("/dinamik_koaksil2", methods = ["POST", "GET"])
def koaksial_dinamik2():
    if request.form["Poisk1"] == "Poisk":
        if request.method == "POST":
            poisk = request.form["Poisk"].upper()
            print(poisk)
            cursor.execute(f"SELECT Dinamik_Koaksil.id, Производитель, Модель, Цена, Image, Types_dinamik_koaksil.Razmer_type FROM Dinamik_Koaksil INNER JOIN Types_dinamik_koaksil ON Types_dinamik_koaksil.id = Dinamik_Koaksil.Type_Razmer WHERE Модель LIKE '%{poisk}%' ")
            r = cursor.fetchall()
            page = 2
            link = "/dinamik_koaksil1"
            return render_template("tovar.html", r=r, pag = page, info = "Магнитола",  link = link, type = "koaksil_dinamik")
    else:
        cursor.execute("SELECT Dinamik_Koaksil.id, Производитель, Модель, Цена, Image, Types_dinamik_koaksil.Razmer_type FROM Dinamik_Koaksil INNER JOIN Types_dinamik_koaksil ON Types_dinamik_koaksil.id = Dinamik_Koaksil.Type_Razmer WHERE Dinamik_Koaksil.id > 15 and Dinamik_Koaksil.id < 31")
        r = cursor.fetchall()
        page = 2
        link = "/dinamik_koaksil1"
        return render_template("tovar.html", r=r, pag = page, info = "Динамик коаксиальный", link = link, type = "koaksil_dinamik")

@f.route("/sabvyfoofer", methods = ["POST", "GET"])
def sabik1():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT SABVOOFER.id, Производитель, Модель, Цена, Image, Types_SAB.Type FROM SABVOOFER INNER JOIN Types_SAB ON Types_SAB.id = SABVOOFER.Types_SAB WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 1
        link = "/sabvyfoofer2"
        return render_template("tovar.html", r=r, pag = page, info = "Сабвуферы", link = link, type = "sabvyfoofer")
    else:
        cursor.execute("SELECT SABVOOFER.id, Производитель, Модель, Цена, Image, Types_SAB.Type FROM SABVOOFER INNER JOIN Types_SAB ON Types_SAB.id = SABVOOFER.Types_SAB WHERE SABVOOFER.id < 16")
        r = cursor.fetchall()
        page = 1
        link = "/sabvyfoofer2"
        return render_template("tovar.html", r=r, pag = page, info = "Сабвуферы", link=link, type = "sabvyfoofer")

@f.route("/sabvyfoofer2", methods = ["POST", "GET"])
def sabik2():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT SABVOOFER.id, Производитель, Модель, Цена, Image, Types_SAB.Type FROM SABVOOFER INNER JOIN Types_SAB ON Types_SAB.id = SABVOOFER.Types_SAB WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 2
        link = "/sabvyfoofer"
        return render_template("tovar.html", r=r, pag = page, info = "Сабвуферы", link = link, type = "sabvyfoofer")
    else:
        cursor.execute("SELECT SABVOOFER.id, Производитель, Модель, Цена, Image, Types_SAB.Type FROM SABVOOFER INNER JOIN Types_SAB ON Types_SAB.id = SABVOOFER.Types_SAB WHERE SABVOOFER.id > 15 and SABVOOFER.id < 31")
        r = cursor.fetchall()
        page = 2
        link = "/sabvyfoofer"
        return render_template("tovar.html", r=r, pag = page, info = "Сабвуферы", link=link, type = "sabvyfoofer")

@f.route("/ysiliteli", methods = ["POST", "GET"])
def Ysiliteli1():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Ysiliteli.id, Производитель, Модель, Цена, Image, Ysiliteli_type.Type FROM Ysiliteli INNER JOIN Ysiliteli_type ON Ysiliteli_type.id =  Ysiliteli.Type_kanal WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 1
        link = "/ysiliteli2"
        return render_template("tovar.html", r=r, pag = page, info = "Усилители", link = link, type = "ysiliteli")
    else:
        cursor.execute("SELECT Ysiliteli.id, Производитель, Модель, Цена, Image, Ysiliteli_type.Type FROM Ysiliteli INNER JOIN Ysiliteli_type ON Ysiliteli_type.id =  Ysiliteli.Type_kanal WHERE Ysiliteli.id < 16")
        r = cursor.fetchall()
        page = 1
        link = "/ysiliteli2"
        return render_template("tovar.html", r=r, pag=page, info = "Усилители", link=link, type = "ysiliteli")

@f.route("/ysiliteli2", methods = ["POST", "GET"])
def Ysiliteli2():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Ysiliteli.id, Производитель, Модель, Цена, Image, Ysiliteli_type.Type FROM Ysiliteli INNER JOIN Ysiliteli_type ON Ysiliteli_type.id =  Ysiliteli.Type_kanal WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 2
        link = "/ysiliteli"
        return render_template("tovar.html", r=r, pag = page, info = "Усилители", link = link, type = "ysiliteli")
    else:
        cursor.execute("SELECT Ysiliteli.id, Производитель, Модель, Цена, Image, Ysiliteli_type.Type FROM Ysiliteli INNER JOIN Ysiliteli_type ON Ysiliteli_type.id =  Ysiliteli.Type_kanal WHERE Ysiliteli.id > 15 and Ysiliteli.id < 31")
        r = cursor.fetchall()
        page = 2
        link = "/ysiliteli"
        return render_template("tovar.html", r=r, pag=page, info = "Усилители", link=link, type = "ysiliteli")

@f.route("/product_single/koaksil_dinamik/<int:id>")
def product1(id):
    # cursor.execute(f"SELECT id, Производитель, Модель, [Номинальная мощность], [Максимальная мощность], Сопротивление, [Диапозон частот], Чувствительность, [Вес магнита], Type_Razmer, Цена, Image FROM Dinamik_Koaksil  WHERE id = {id}")
    cursor.execute(f"SELECT * FROM Dinamik_Koaksil WHERE id = {id}")
    r = cursor.fetchone()
    r = list(r)
    return render_template("product_single.html", r=r)

@f.route("/product_single/magnitola/<int:id>")
def product2(id):
    cursor.execute(f"SELECT Magnitofon.id, Производитель, Модель, Image, Bluetooth, Aux, USB, Цена, [Выходная мощность на канал], Радиоприемник FROM Magnitofon WHERE id = {id}")
    r = cursor.fetchone()
    r = list(r)
    if r[4] == True:
        r[4]="Bluetooth: Есть"
    else:
        r[4] = "Bluetooth: Нет"

    if r[5] == True:
        r[5]="Aux: Есть"
    else:
        r[5] = "Aux: Нет"

    if r[6] == True:
        r[6]="USB: Есть"
    else:
        r[6] = "USB: Нет"

    if r[9] == True:
        r[9]="Радиоприемник: Есть"
    else:
        r[9] = "Радиоприемник: Нет"

    return render_template("product_single.html", r=r)


@f.route("/product_single/Oval/<int:id>")
def product0(id):
    cursor.execute(f"SELECT * FROM Dinamik_OVAL WHERE id = {id}")
    r = cursor.fetchone()
    r = list(r)
    return render_template("product_single.html", r=r)

@f.route("/product_single/krossover/<int:id>")
def product3(id):
    cursor.execute(f"SELECT * FROM Dinamik_Krossover WHERE id = {id}")
    r = cursor.fetchone()
    r = list(r)
    return render_template("product_single.html", r=r)

@f.route("/product_single/sab_in_korob/<int:id>")
def product4(id):
    cursor.execute(f"SELECT * FROM Aktivn_SAB_IN_KOROB WHERE id = {id}")
    r = cursor.fetchone()
    r = list(r)
    return render_template("product_single.html", r=r)

@f.route("/product_single/sabvyfoofer/<int:id>")
def product5(id):
    cursor.execute(f"SELECT * FROM SABVOOFER WHERE id = {id}")
    r = cursor.fetchone()
    r = list(r)
    return render_template("product_single.html", r=r)


@f.route("/product_single/ysiliteli/<int:id>")
def product6(id):
    cursor.execute(f"SELECT * FROM Ysiliteli WHERE id = {id}")
    r = cursor.fetchone()
    r = list(r)
    if r[4] == True:
        r[4] = "Широкополсная область применения: Есть"
    else:
        r[4] = "Широкополсной области применения: Нет"
    
    if r[5] == True:
        r[5] = "Область применения для сабвуфера: Есть"
    else:
        r[5] = "Области применеия для сабвуфера: Нет"

    return render_template("product_single.html", r=r)

@f.route("/product_single/twitter/<int:id>")
def product7(id):
    cursor.execute(f"SELECT * FROM Tvitter_dinamik WHERE id = {id}")
    r = cursor.fetchone()
    r = list(r)
    return render_template("product_single.html", r=r)

@f.route("/product_single/komponent_dinamik/<int:id>")
def product8(id):
    cursor.execute(f"SELECT Dinamik_Komponent.id, Производитель, Модель, Image, [Номинальная мощность], [Максимальная мощность], Сопротивление, Цена, [Диапозон частот], Чувствительность FROM Dinamik_Komponent INNER JOIN Dinamik_komponent_TYPE ON Dinamik_Komponent.Type_Razmer = Dinamik_Komponent_TYPE.id WHERE Dinamik_Komponent.id = {id}")
    r = cursor.fetchone()
    r = list(r)
    return render_template("product_single.html", r=r)

@f.route("/krossover", methods = ["POST", "GET"])
def Krossover1():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Dinamik_Krossover.id, Производитель, Модель, Цена, Dinamik_Krossover_Type.Type_Razmer FROM Dinamik_Krossover INNER JOIN Dinamik_Krossover_Type ON Dinamik_Krossover_Type.id = Dinamik_Krossover.Type_Razmer WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 1
        link = "/krossover2"
        return render_template("tovar.html", r=r, pag = page, info = "Кроссоверы", link = link, type = "krossover")
    else:
        cursor.execute("SELECT Dinamik_Krossover.id, Производитель, Модель, Цена, Dinamik_Krossover_Type.Type_Razmer FROM Dinamik_Krossover INNER JOIN Dinamik_Krossover_Type ON Dinamik_Krossover_Type.id = Dinamik_Krossover.Type_Razmer WHERE Dinamik_Krossover.id < 16")
        r = cursor.fetchall()
        page = 1
        link = "/krossover2"
        return render_template("tovar.html", r=r, pag=page, info = "Кроссоверы", link = link, type = "krossover")

@f.route("/krossover2", methods = ["POST", "GET"])
def Krossover2():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Dinamik_Krossover.id, Производитель, Модель, Цена, Dinamik_Krossover_Type.Type_Razmer FROM Dinamik_Krossover INNER JOIN Dinamik_Krossover_Type ON Dinamik_Krossover_Type.id = Dinamik_Krossover.Type_Razmer WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 2
        link = "/krossover"
        return render_template("tovar.html", r=r, pag = page, info = "Кроссоверы", link = link, type = "krossover")
    else:    
        cursor.execute("SELECT Dinamik_Krossover.id, Производитель, Модель, Цена, Dinamik_Krossover_Type.Type_Razmer FROM Dinamik_Krossover INNER JOIN Dinamik_Krossover_Type ON Dinamik_Krossover_Type.id = Dinamik_Krossover.Type_Razmer WHERE Dinamik_Krossover.id > 15 and Dinamik_Krossover.id < 31")
        r = cursor.fetchall()
        page = 2
        link = "/krossover"
        return render_template("tovar.html", r=r, pag=page, info = "Кроссоверы", link = link, type = "krossover")

@f.route("/sab_in_korob", methods = ["POST", "GET"])
def sab_in_korob1():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Aktivn_SAB_IN_KOROB.id, Производитель, Модель, Image, Цена, Aktivn_SAB_IN_KOROB.Types_SAB FROM Aktivn_SAB_IN_KOROB INNER JOIN Types_SAB ON Types_SAB.id = Aktivn_SAB_IN_KOROB.Types_SAB WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 1
        link = "/sab_in_korob2"
        return render_template("tovar.html", r=r, pag = page, info = "Сабвуферы в коробе", link = link, type = "sab_in_korob")
    else:
        cursor.execute("SELECT Aktivn_SAB_IN_KOROB.id, Производитель, Модель, Image, Цена, Aktivn_SAB_IN_KOROB.Types_SAB FROM Aktivn_SAB_IN_KOROB INNER JOIN Types_SAB ON Types_SAB.id = Aktivn_SAB_IN_KOROB.Types_SAB WHERE Aktivn_SAB_IN_KOROB.id < 16 ")
        r = cursor.fetchall()
        page = 1
        link = "/sab_in_korob2"
        return render_template("tovar.html", r=r, pag=page, info = "Сабвуферы в коробе", link=link, type = "sab_in_korob")

@f.route("/sab_in_korob2", methods = ["POST", "GET"])
def sab_in_korob2():
    if request.method == "POST":
        poisk = request.form["Poisk"].upper()
        print(poisk)
        cursor.execute(f"SELECT Aktivn_SAB_IN_KOROB.id Производитель, Модель, Image, Цена, Aktivn_SAB_IN_KOROB.Types_SAB FROM Aktivn_SAB_IN_KOROB INNER JOIN Types_SAB ON Types_SAB.id = Aktivn_SAB_IN_KOROB.Types_SAB WHERE Модель LIKE '%{poisk}%' ")
        r = cursor.fetchall()
        page = 2
        link = "/sab_in_korob"
        return render_template("tovar.html", r=r, pag = page, info = "Сабвуферы в коробе", link = link, type = "sab_in_korob")
    else:
        cursor.execute("SELECT Aktivn_SAB_IN_KOROB.id Производитель, Модель, Image, Цена, Aktivn_SAB_IN_KOROB.Types_SAB FROM Aktivn_SAB_IN_KOROB INNER JOIN Types_SAB ON Types_SAB.id = Aktivn_SAB_IN_KOROB.Types_SAB WHERE Aktivn_SAB_IN_KOROB.id > 15 and Aktivn_SAB_IN_KOROB.id < 31 ")
        r = cursor.fetchall()
        page = 2
        link = "/sab_in_korob"
        return render_template("tovar.html", r=r, pag=page, info = "Сабвуферы в коробе", link = link, type = "sab_in_korob")

@f.route("/register", methods = ["POST", "GET"])
def register():

    if request.method == "POST":
        name = request.form["Name_user"]
        surname = request.form["Surname"]
        nomer = request.form["Nomer"]
        email = request.form["Email"]
        login = request.form["Login"]
        password = request.form["Password"]
        password_two = request.form["Password_two"]
        print(password)
        print(password_two)
        if password != password_two:
            return render_template("Reg.html")
        else:
          
            l = db.USERS(Email = email, Password = password, Login = login, Name_user = name, Surname = surname, Nomer = nomer)
            db.session.add(l)
            db.session.commit()
            return redirect("/")
        
            # return "При заполнении записи произошла ошибка"
    else:    
        return render_template("Reg.html")









if __name__ == "__main__":
    f.run(debug=True)