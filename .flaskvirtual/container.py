from flask import *

news = [
    {
        'title': 'Первая запись',  
        'text': 'Много-много текста',  
        'date': '10 Мая 2020',  
        'author': 'Валерий'  
    },  
    {  
        'title': 'Вторая запись',  
        'text': 'Снова много-много текста',  
        'date': '19 Мая 2020',  
        'author': 'Егор'  

    }  
]  

f = Flask(__name__)

f.route("/index", methods = ["POST"])
def lp():
    return render_template("container.html")



if __name__ == "__main__":
    f.run(debug=True)