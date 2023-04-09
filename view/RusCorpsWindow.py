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
        # задаем возможные варианты для первого батальона
        bttln_list = self.presenter.rusLineInfantryBrigadeBttlnList(0)
        for bttlnName in bttln_list:
            self.aBrgdFirstBattalion.addItem(bttlnName)
        # задаем возможные варианты для второго батальона
        bttln_list = self.presenter.rusLineInfantryBrigadeBttlnList(1)
        for bttlnName in bttln_list:
            self.aBrgdSecondBattalion.addItem(bttlnName)
        # задаем возможные варианты для третьего батальона
        bttln_list = self.presenter.rusLineInfantryBrigadeBttlnList(2)
        for bttlnName in bttln_list:
            self.aBrgdThirdBattalion.addItem(bttlnName)
        # задаем возможные варианты для четвертого батальона
        bttln_list = self.presenter.rusLineInfantryBrigadeBttlnList(3)
        for bttlnName in bttln_list:
            self.aBrgdFourthBattalion.addItem(bttlnName)
        # задаем возможные варианты для дополнительного батальона
        bttln_list = self.presenter.rusLineInfantryBrigadeBttlnList(4)
        for bttlnName in bttln_list:
            self.aBrgdAdditionalBattalion.addItem(bttlnName)


    def aBrgd1stBttlnCostView(self, index):
# отправляем индекс в презентер для передачи в модель чтобы поместить соотетствующий батальон на его место в бригаде
        order_number = 0 # порядковое место в бригаде
        bttln_choosen_from_list = index # индекс выбранного баталльона из списка
        self.presenter.rusLineInfantryBrigadeBttlnChoosen (order_number, bttln_choosen_from_list)
# отправляем запрос стоимости батальона стоящего на соответствующем месте в бригаде
        value = self.presenter.rusLineInfantryBrigadeBttlnCost(order_number)
# записываем в соответствующее поле значение стоимости батальона
        self.aBrgdFirstBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgd2ndBttlnCostView(self, index):
        order_number = 1
        bttln_choosen_from_list = index
        self.presenter.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter.rusLineInfantryBrigadeBttlnCost(order_number)
        self.aBrgdSecondBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgd3rdBttlnCostView(self, index):
        order_number = 2
        bttln_choosen_from_list = index
        self.presenter.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter.rusLineInfantryBrigadeBttlnCost(order_number)
        self.aBrgdThirdBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgd4thBttlnCostView(self, index):
        order_number = 3
        bttln_choosen_from_list = index
        self.presenter.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter.rusLineInfantryBrigadeBttlnCost(order_number)
        self.aBrgdFourthBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgdAddBttlnCostView(self, index):
        order_number = 4
        bttln_choosen_from_list = index
        self.presenter.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter.rusLineInfantryBrigadeBttlnCost(order_number)
        self.aBrgdAddBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgdTotalCostView(self):

        bttln1_cost = self.presenter.rusLineInfantryBrigadeBttlnCost(0)
        bttln2_cost = self.presenter.rusLineInfantryBrigadeBttlnCost(1)
        bttln3_cost = self.presenter.rusLineInfantryBrigadeBttlnCost(2)
        bttln4_cost = self.presenter.rusLineInfantryBrigadeBttlnCost(3)
        bttlnAdd_cost = self.presenter.rusLineInfantryBrigadeBttlnCost(4)
        total_cost = bttln1_cost+bttln2_cost+bttln3_cost+bttln4_cost+bttlnAdd_cost
        self.aBrgdTotalCost.setText(str(total_cost))

    def the_button_was_clicked(self):

        if self.aBrgdFirstBattalion.currentIndex()!=0:
            self.bonus_window = BonusWindow()
            self.bonus_window.setWindowTitle("First Battalion")

            self.bonus_window.name.setText(str(self.presenter.rusLineInfantryBrigadeBttlnName(0)))
            self.bonus_window.cost.setText(str(self.presenter.rusLineInfantryBrigadeBttlnCost(0)))

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
