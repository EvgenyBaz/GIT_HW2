# pyuic6 StartGuiWindow.ui -o StartGuiWindow.py
# pyuic6 RusDivisionGuiWindow.ui -o RusDivisionGuiWindow.py
# pyuic6 LineInfantryBonusGuiWindow.ui -o LineInfantryBonusGuiWindow.py

from PyQt6 import QtGui
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt6 import QtWidgets, uic

from view.StartWindow import StartWindow
from view.RusDivisionWindow import RusDivisionWindow

class MainWindow(QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.setupUi(self)


    def show_StartWindow(self):
        self.startWindow = StartWindow()
        self.startWindow.setWindowTitle("Black Powder 2.0 Army Builder")

        self.startWindow.pushButton_Russia.clicked.connect(self.show_RusDivisionWindow) # по нажатию кнопки включаем окно с описанием корпуса русской армии
        self.startWindow.pushButton_Russia.clicked.connect(self.startWindow.close) # выключаем текущее окно
        self.startWindow.pushButton_France.clicked.connect(self.the_fra_button_was_clicked) # заглушка
        self.startWindow.show()


    def show_RusDivisionWindow(self):
        self.rusDivisionWindow = RusDivisionWindow()
        self.rusDivisionWindow.setWindowTitle("Black Powder 2.0 Army Builder")

        self.rusDivisionWindow.generalCost.setText("0")
        self.rusDivisionWindow.aBrgdTotalCost.setText("0")
        self.rusDivisionWindow.bBrgdTotalCost.setText("0")
        self.rusDivisionWindow.cBrgdTotalCost.setText("0")
        self.rusDivisionWindow.JgrBrgdTotalCost.setText("0")
        self.rusDivisionWindow.CombGrndrBrgdTotalCost.setText("0")

        self.rusDivisionWindow.division_cmndrs_list()
        self.rusDivisionWindow.a_brigade_bttln_Lists()
        self.rusDivisionWindow.b_brigade_bttln_Lists()
        self.rusDivisionWindow.c_brigade_bttln_Lists()
        self.rusDivisionWindow.jgr_brigade_bttln_Lists()
        self.rusDivisionWindow.comb_grndr_brigade_bttln_Lists()

        self.rusDivisionWindow.show()


    def the_fra_button_was_clicked(self): # заглушка
        print("fra_clicked")




app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show_StartWindow()
app.exec()
