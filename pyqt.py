from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def app():
    pril = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("приложение")
    window.setGeometry(300, 400, 300, 500)
    
    label = QtWidgets.QLabel(window)
    label.setText("Приветствую, меня зовут Айдер, мне 17 лет")
    label.move(250, 100)
    label.adjustSize()
    Button = QtWidgets.QPushButton(window)
    Button.setText("Пуск")
    Button.move(50, 75)
    Button.setFixedWidth(100)
    Button.clicked.connect(Button_click)
    
    window.show()
    sys.exit(pril.exec_())


def Button_click():
    print("Hello word")


if __name__ == "__main__":
    app()