#Это основной файл и в нем будет реализовано окно программы с помощью библиотеки PyQT6
from PyQt6 import QtCore, QtGui, QtWidgets
import sys


def create_description():
    """
    Функция создает описание программы
    :return: Описание программы
    """
    return "" \
           "я еще пока не знаю точно какая будет програ, но все варианты и тз можно писать сюда)))\n" \
           "1. Оконное приложение для компьютера\n" \
           "2. ..."


print(create_description())


class MainWindow(QtWidgets.QMainWindow): #Создание окна приложения

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)                              #Определяем метод родительского класса
        self.setGeometry(100, 100, 400, 300)                                           #Определяем размер окна
        self.setWindowTitle("Программа")                                               #Определяем название окна
        self.setWindowIcon(QtGui.QIcon("program_icon.jpg"))                            #Определяем иконку окна
        self.setFixedSize(400, 300)                                                    #Определяем размер окна
        self.setCentralWidget(QtWidgets.QWidget(self))                                 #Определяем окно с классом





if __name__ == "__main__":                                                             # Инициализируем запуск Приложения
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())