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
        brgd_ist = self.presenter.rusLineInfantryBrigadeCorrList()
        for btln in brgd_ist:
            self.firstBatallion.addItem(btln.name) # тут переписать . Из презентера должны возвращаться только ссписки имен
#надо сделать обработчик где из списка бригады достаются только имена , только стоимосить и тд в виде списков и кним обращаться
