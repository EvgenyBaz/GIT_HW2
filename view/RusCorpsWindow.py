from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout
import sys

from presenter import Presenter
from view.RusCorpsGuiWindow import Ui_RusCorpsWindow
from view.BonusWindow import BonusWindow

# from RusCorpsGuiWindow import Ui_RusCorpsWindow


class RusCorpsWindow(QtWidgets.QMainWindow, Ui_RusCorpsWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(RusCorpsWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.presenter = Presenter()

        self.aBrgdFirstBattalion.currentIndexChanged.connect(self.aBrgd1stBttlnCostView)
        self.aBrgdSecondBattalion.currentIndexChanged.connect(self.aBrgd2ndBttlnCostView)
        self.aBrgdThirdBattalion.currentIndexChanged.connect(self.aBrgd3rdBttlnCostView)
        self.aBrgdFourthBattalion.currentIndexChanged.connect(self.aBrgd4thBttlnCostView)
        self.aBrgdAdditionalBattalion.currentIndexChanged.connect(self.aBrgdAddBttlnCostView)

        self.aBrFirstBttlnModPushButton.clicked.connect(self.the_button_was_clicked)

    def brigade_bttln_Lists(self):
        bttln_list = self.presenter.rusLineInfantryBrigade1stBttlnList()
        for bttlnName in bttln_list:
            self.aBrgdFirstBattalion.addItem(bttlnName)

        bttln_list = self.presenter.rusLineInfantryBrigade2ndBttlnList()
        for bttlnName in bttln_list:
            self.aBrgdSecondBattalion.addItem(bttlnName)

        bttln_list = self.presenter.rusLineInfantryBrigade3rdBttlnList()
        for bttlnName in bttln_list:
            self.aBrgdThirdBattalion.addItem(bttlnName)

        bttln_list = self.presenter.rusLineInfantryBrigade4thBttlnList()
        for bttlnName in bttln_list:
            self.aBrgdFourthBattalion.addItem(bttlnName)

        bttln_list = self.presenter.rusLineInfantryBrigadeAddList()
        for btlnName in bttln_list:
            self.aBrgdAdditionalBattalion.addItem(btlnName)
    def aBrgd1stBttlnCostView(self, index):

        value = self.presenter.rusLineInfantryBrigade1stBttlnCost(index)
        self.aBrgdFirstBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgd2ndBttlnCostView(self, index):

        value = self.presenter.rusLineInfantryBrigade2ndBttlnCost(index)
        self.aBrgdSecondBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgd3rdBttlnCostView(self, index):

        value = self.presenter.rusLineInfantryBrigade3rdBttlnCost(index)
        self.aBrgdThirdBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgd4thBttlnCostView(self, index):

        value = self.presenter.rusLineInfantryBrigade4thBttlnCost(index)
        self.aBrgdFourthBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgdAddBttlnCostView(self, index):

        value = self.presenter.rusLineInfantryBrigadeAddBttlnCost(index)
        self.aBrgdAddBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgdTotalCostView(self):

        bttln1_cost = self.presenter.rusLineInfantryBrigade1stBttlnCost(self.aBrgdFirstBattalion.currentIndex())
        bttln2_cost = self.presenter.rusLineInfantryBrigade2ndBttlnCost(self.aBrgdSecondBattalion.currentIndex())
        bttln3_cost = self.presenter.rusLineInfantryBrigade3rdBttlnCost(self.aBrgdThirdBattalion.currentIndex())
        bttln4_cost = self.presenter.rusLineInfantryBrigade4thBttlnCost(self.aBrgdFourthBattalion.currentIndex())
        bttlnAdd_cost = self.presenter.rusLineInfantryBrigadeAddBttlnCost(self.aBrgdAdditionalBattalion.currentIndex())
        total_cost = bttln1_cost+bttln2_cost+bttln3_cost+bttln4_cost+bttlnAdd_cost
        self.aBrgdTotalCost.setText(str(total_cost))

    def the_button_was_clicked(self):

        if self.aBrgdFirstBattalion.currentIndex()!=0:
            self.bonus_window = BonusWindow()
            self.bonus_window.setWindowTitle("First Battalion")
            self.bonus_window.name.setText(self.presenter.rusLineInfantryBrigade1stBttlnList()[self.aBrgdFirstBattalion.currentIndex()])

            self.bonus_window.cost.setText(str(self.presenter.rusLineInfantryBrigade1stBttlnCost(self.aBrgdFirstBattalion.currentIndex())))



            self.bonus_window.ok_button.clicked.connect(self.ok_button_was_clicked)
            self.bonus_window.cancel_button.clicked.connect(self.cancel_button_was_clicked)
            self.bonus_window.show()

    def ok_button_was_clicked(self):
        if self.aBrgdFirstBattalion.currentIndex() != 0:
            print ("данные сохранены")
            self.bonus_window.close()
        else:
            self.cancel_button_was_clicked()

    def cancel_button_was_clicked(self):
        self.bonus_window.close()
