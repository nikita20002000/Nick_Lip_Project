# Это основной файл и в нем будет реализовано окно программы с помощью библиотеки PyQT6

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.mainW import Ui_MainWindow
from Window.developer_info import Ui_Dialog


def create_description():
    """
    Функция создает описание программы
    :return: Описание программы
    """
    return "" \
           "я еще пока не знаю точно какая будет програ, но все варианты и тз можно писать сюда💩\n" \
           "1. Оконное приложение для компьютера\n" \
           "2. Добавим основной функционал:\n" \
           "\t-возможность генерации титульников!\n" \
           "\t-возможность просмотривать дз и дедлайны?\n" \
           "\t-новостная лента?\n" \
           "\t-можно создать внутри базу данных с литературой?\n"


class developers_window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(developers_window, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon())


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)

        self.action.triggered.connect(self.show_developer_info)  ##подключил кнопку вывода инфы про разработчиков

    def show_developer_info(self):
        self.Dialog = developers_window()
        self.Dialog.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())
