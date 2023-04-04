import pytest

import Window.mainW
from Window.titul_generate import Ui_Dialog_3
from Functional.funcdoc import create_titul
from main import titul_generate_window
from PyQt5 import QtCore, QtGui, QtWidgets



class TestMainW:
    def test_that_generating_titul_runned_successfully(self):
        s = create_titul('name1', "first_name1", "last_name1", "group1", 1)
        assert s == 1

