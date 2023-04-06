from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout

from presenter import Presenter
from view.RusCorpsGuiWindow import Ui_RusCorpsWindow
# from RusCorpsGuiWindow import Ui_RusCorpsWindow


class RusCorpsWindow(QtWidgets.QMainWindow, Ui_RusCorpsWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(RusCorpsWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.presenter = Presenter()

    def brigadeLists(self):
        brgd_list = self.presenter.rusLineInfantryBrigadeCoreList()
        for btlnName in brgd_list:
            self.aBrgdFirstBatallion.addItem(btlnName)
            self.aBrgdSecondfirstBatallion.addItem(btlnName)
            self.aBrgdThirdBatallion.addItem(btlnName)
            self.aBrgdFourthBatallion.addItem(btlnName)
    def brigadeAdditionalList(self):
        brgd_list = self.presenter.rusLineInfantryBrigadeAddList()
        for btlnName in brgd_list:
            self.aBrgdAdditionalBatallion.addItem(btlnName)