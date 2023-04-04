# Это основной файл и в нем будет реализовано окно программы с помощью библиотеки PyQT5

from PyQt5 import QtCore, QtGui, QtWidgets
from Window.mainW import Ui_MainWindow
from Window.developer_info import Ui_Dialog
from Window.about_programm import Ui_Dialog_1
from Window.donate import Ui_Dialog_2
from Window.titul_generate import Ui_Dialog_3
from Functional.funcdoc import create_titul



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

class about_programm(QtWidgets.QDialog, Ui_Dialog_1):
    def __init__(self, parent=None):
        super(about_programm, self).__init__()
        self.setupUi_1(self)
        self.setWindowIcon(QtGui.QIcon())

class donate(QtWidgets.QDialog, Ui_Dialog_2):
    def __init__(self, parent=None):
        super(donate, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon())

class titul_generate_window(QtWidgets.QDialog, Ui_Dialog_3):
    def __init__(self, parent=None):
        super(titul_generate_window, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon())

        self.pushButton.clicked.connect(self.get_titul_info)


    def get_titul_info(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        lastname = self.lineEdit_4.text()
        group = self.lineEdit_3.text()
        position_in_sub_list = 0

        for i in range(len(self.mass_of_subjects)):
            if self.mass_of_subjects[i].isChecked():
                position_in_sub_list = i
                break

        create_titul(name, surname, lastname, group, position_in_sub_list)




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

        self.pushButton_2.clicked.connect(self.show_titul_generate)
        self.action.triggered.connect(self.show_developer_info)  ##подключил кнопк]]у вывода инфы про разработчиков
        self.actionEduHelper.triggered.connect(self.show_about_programm)  ##подключ
        self.action_2.triggered.connect(self.show_donates)  ##подключил

    def show_developer_info(self):
        self.Dialog = developers_window()
        self.Dialog.show()

    def show_about_programm(self):
        self.Dialog_1 = about_programm()
        self.Dialog_1.show()
    def show_donates(self):
        self.Dialog_2 = donate()
        self.Dialog_2.show()
    def show_titul_generate(self):
        self.Dialog_3 = titul_generate_window()
        self.Dialog_3.show()








if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())
