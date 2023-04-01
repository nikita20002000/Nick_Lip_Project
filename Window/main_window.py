from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class MainWindow(QtWidgets.QMainWindow):  # Создание окна приложения

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)  # Определяем метод родительского класса
        self.setGeometry(100, 100, 400, 300)  # Определяем размер окна
        self.setWindowTitle("Программа")  # Определяем название окна
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))  # Определяем иконку окна
        self.setFixedSize(400, 300)  # Определяем размер окна
        self.setCentralWidget(QtWidgets.QWidget(self))  # Определяем окно с классом


def create_app():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())