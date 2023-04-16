from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout
import sys

from presenter import Presenter
from view.RusCorpsGuiWindow import Ui_RusCorpsWindow
from view.BonusWindow import BonusWindow


class RusCorpsWindow(QtWidgets.QMainWindow, Ui_RusCorpsWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(RusCorpsWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.presenter1 = Presenter()

        self.aBrgdCmndr.currentIndexChanged.connect(self.aBrgdCommanderCostView)
        self.aBrgdFirstBattalion.currentIndexChanged.connect(self.aBrgd1stBttlnCostView)
        self.aBrgdSecondBattalion.currentIndexChanged.connect(self.aBrgd2ndBttlnCostView)
        self.aBrgdThirdBattalion.currentIndexChanged.connect(self.aBrgd3rdBttlnCostView)
        self.aBrgdFourthBattalion.currentIndexChanged.connect(self.aBrgd4thBttlnCostView)
        self.aBrgdAdditionalBattalion.currentIndexChanged.connect(self.aBrgdAddBttlnCostView)

        self.aBrFirstBttlnModPushButton.clicked.connect(self.a_the_first_bttln_mod_button_was_clicked)
        self.aBrSecondBttlnModPushButton.clicked.connect(self.a_the_second_bttln_mod_button_was_clicked)
        self.aBrThirdBttlnModPushButton.clicked.connect(self.a_the_third_bttln_mod_button_was_clicked)
        self.aBrFourthBttlnModPushButton.clicked.connect(self.a_the_fourth_bttln_mod_button_was_clicked)
        self.aBrAddBttlnModPushButton.clicked.connect(self.a_the_add_bttln_mod_button_was_clicked)

        self.presenter2 = Presenter()

        self.bBrgdCmndr.currentIndexChanged.connect(self.bBrgdCommanderCostView)
        self.bBrgdFirstBattalion.currentIndexChanged.connect(self.bBrgd1stBttlnCostView)
        self.bBrgdSecondBattalion.currentIndexChanged.connect(self.bBrgd2ndBttlnCostView)
        self.bBrgdThirdBattalion.currentIndexChanged.connect(self.bBrgd3rdBttlnCostView)
        self.bBrgdFourthBattalion.currentIndexChanged.connect(self.bBrgd4thBttlnCostView)
        self.bBrgdAdditionalBattalion.currentIndexChanged.connect(self.bBrgdAddBttlnCostView)

        self.bBrFirstBttlnModPushButton.clicked.connect(self.b_the_first_bttln_mod_button_was_clicked)
        self.bBrSecondBttlnModPushButton.clicked.connect(self.b_the_second_bttln_mod_button_was_clicked)
        self.bBrThirdBttlnModPushButton.clicked.connect(self.b_the_third_bttln_mod_button_was_clicked)
        self.bBrFourthBttlnModPushButton.clicked.connect(self.b_the_fourth_bttln_mod_button_was_clicked)
        self.bBrAddBttlnModPushButton.clicked.connect(self.b_the_add_bttln_mod_button_was_clicked)

        self.presenter3 = Presenter()

        self.cBrgdCmndr.currentIndexChanged.connect(self.cBrgdCommanderCostView)
        self.cBrgdFirstBattalion.currentIndexChanged.connect(self.cBrgd1stBttlnCostView)
        self.cBrgdSecondBattalion.currentIndexChanged.connect(self.cBrgd2ndBttlnCostView)
        self.cBrgdThirdBattalion.currentIndexChanged.connect(self.cBrgd3rdBttlnCostView)
        self.cBrgdFourthBattalion.currentIndexChanged.connect(self.cBrgd4thBttlnCostView)
        self.cBrgdAdditionalBattalion.currentIndexChanged.connect(self.cBrgdAddBttlnCostView)

        self.cBrFirstBttlnModPushButton.clicked.connect(self.c_the_first_bttln_mod_button_was_clicked)
        self.cBrSecondBttlnModPushButton.clicked.connect(self.c_the_second_bttln_mod_button_was_clicked)
        self.cBrThirdBttlnModPushButton.clicked.connect(self.c_the_third_bttln_mod_button_was_clicked)
        self.cBrFourthBttlnModPushButton.clicked.connect(self.c_the_fourth_bttln_mod_button_was_clicked)
        self.cBrAddBttlnModPushButton.clicked.connect(self.c_the_add_bttln_mod_button_was_clicked)

    def a_brigade_bttln_Lists(self):
        # задаем возможны варианты имен командиров
        cmndrs_list = self.presenter1.rusLineInfantryBrigadeCmndrsNamesList()
        for cmndrName in cmndrs_list:
            self.aBrgdCmndr.addItem(cmndrName)
        # задаем возможные варианты для первого батальона
        bttln_list = self.presenter1.rusLineInfantryBrigadeBttlnList(0)
        for bttlnName in bttln_list:
            self.aBrgdFirstBattalion.addItem(bttlnName)
        # задаем возможные варианты для второго батальона
        bttln_list = self.presenter1.rusLineInfantryBrigadeBttlnList(1)
        for bttlnName in bttln_list:
            self.aBrgdSecondBattalion.addItem(bttlnName)
        # задаем возможные варианты для третьего батальона
        bttln_list = self.presenter1.rusLineInfantryBrigadeBttlnList(2)
        for bttlnName in bttln_list:
            self.aBrgdThirdBattalion.addItem(bttlnName)
        # задаем возможные варианты для четвертого батальона
        bttln_list = self.presenter1.rusLineInfantryBrigadeBttlnList(3)
        for bttlnName in bttln_list:
            self.aBrgdFourthBattalion.addItem(bttlnName)
        # задаем возможные варианты для дополнительного батальона
        bttln_list = self.presenter1.rusLineInfantryBrigadeBttlnList(4)
        for bttlnName in bttln_list:
            self.aBrgdAdditionalBattalion.addItem(bttlnName)

    def b_brigade_bttln_Lists(self):
        # задаем возможны варианты имен командиров
        cmndrs_list = self.presenter2.rusLineInfantryBrigadeCmndrsNamesList()
        for cmndrName in cmndrs_list:
            self.bBrgdCmndr.addItem(cmndrName)
        # задаем возможные варианты для первого батальона
        bttln_list = self.presenter2.rusLineInfantryBrigadeBttlnList(0)
        for bttlnName in bttln_list:
            self.bBrgdFirstBattalion.addItem(bttlnName)
        # задаем возможные варианты для второго батальона
        bttln_list = self.presenter2.rusLineInfantryBrigadeBttlnList(1)
        for bttlnName in bttln_list:
            self.bBrgdSecondBattalion.addItem(bttlnName)
        # задаем возможные варианты для третьего батальона
        bttln_list = self.presenter2.rusLineInfantryBrigadeBttlnList(2)
        for bttlnName in bttln_list:
            self.bBrgdThirdBattalion.addItem(bttlnName)
        # задаем возможные варианты для четвертого батальона
        bttln_list = self.presenter2.rusLineInfantryBrigadeBttlnList(3)
        for bttlnName in bttln_list:
            self.bBrgdFourthBattalion.addItem(bttlnName)
        # задаем возможные варианты для дополнительного батальона
        bttln_list = self.presenter2.rusLineInfantryBrigadeBttlnList(4)
        for bttlnName in bttln_list:
            self.bBrgdAdditionalBattalion.addItem(bttlnName)

    def c_brigade_bttln_Lists(self):
        # задаем возможны варианты имен командиров
        cmndrs_list = self.presenter3.rusLineInfantryBrigadeCmndrsNamesList()
        for cmndrName in cmndrs_list:
            self.cBrgdCmndr.addItem(cmndrName)
        # задаем возможные варианты для первого батальона
        bttln_list = self.presenter3.rusLineInfantryBrigadeBttlnList(0)
        for bttlnName in bttln_list:
            self.cBrgdFirstBattalion.addItem(bttlnName)
        # задаем возможные варианты для второго батальона
        bttln_list = self.presenter3.rusLineInfantryBrigadeBttlnList(1)
        for bttlnName in bttln_list:
            self.cBrgdSecondBattalion.addItem(bttlnName)
        # задаем возможные варианты для третьего батальона
        bttln_list = self.presenter3.rusLineInfantryBrigadeBttlnList(2)
        for bttlnName in bttln_list:
            self.cBrgdThirdBattalion.addItem(bttlnName)
        # задаем возможные варианты для четвертого батальона
        bttln_list = self.presenter3.rusLineInfantryBrigadeBttlnList(3)
        for bttlnName in bttln_list:
            self.cBrgdFourthBattalion.addItem(bttlnName)
        # задаем возможные варианты для дополнительного батальона
        bttln_list = self.presenter3.rusLineInfantryBrigadeBttlnList(4)
        for bttlnName in bttln_list:
            self.cBrgdAdditionalBattalion.addItem(bttlnName)

    def corpsTotalCostView(self):
        if self.aBrgdTotalCost.text() == "" :
                self.aBrgdTotalCost.setText("0")
        if self.bBrgdTotalCost.text() == "" :
                self.bBrgdTotalCost.setText("0")
        if self.cBrgdTotalCost.text() == "" :
                self.cBrgdTotalCost.setText("0")

        total_cost = int(self.aBrgdTotalCost.text()) + int(self.bBrgdTotalCost.text()) + int(self.cBrgdTotalCost.text())

        self.corpsTotalCost.setText(str(total_cost))

        # отправляем индекс в презентер для передачи в модель чтобы получить стоимост выбранного командира

    def aBrgdCommanderCostView(self, index):
        value = self.presenter1.rusLineInfantryBrigadeCmndrsCost(index)
        self.aBrgdCmndrCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        # отправляем индекс в презентер для передачи в модель чтобы поместить соотетствующий батальон на его место в бригаде
        order_number = 0  # порядковое место в бригаде
        # индекс выбранного баталльона из списка
        self.presenter1.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)
        # отправляем запрос стоимости батальона стоящего на соответствующем месте в бригаде
        value = self.presenter1.rusLineInfantryBrigadeBttlnCost(order_number)
        # записываем в соответствующее поле значение стоимости батальона
        self.aBrgdFirstBattalionCost.setText(str(value))

        self.aBrgdTotalCostView()

    def aBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        order_number = 1
        self.presenter1.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter1.rusLineInfantryBrigadeBttlnCost(order_number)
        self.aBrgdSecondBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        order_number = 2
        self.presenter1.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter1.rusLineInfantryBrigadeBttlnCost(order_number)
        self.aBrgdThirdBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        order_number = 3
        self.presenter1.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter1.rusLineInfantryBrigadeBttlnCost(order_number)
        self.aBrgdFourthBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        order_number = 4
        self.presenter1.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter1.rusLineInfantryBrigadeBttlnCost(order_number)
        self.aBrgdAddBattalionCost.setText(str(value))
        self.aBrgdTotalCostView()

    def aBrgdTotalCostView(self):
        total_cost = self.presenter1.rusLineInfantryBrigadeCmndrsCost(self.aBrgdCmndr.currentIndex()) + \
                     sum(self.presenter1.rusLineInfantryBrigadeBttlnCost(i) for i in range(5))

        self.aBrgdTotalCost.setText(str(total_cost))
        self.corpsTotalCostView()

    def a_the_first_bttln_mod_button_was_clicked(self):

        if self.aBrgdFirstBattalion.currentIndex() != 0:

            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.aBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdFirstBattalionCostSetText = self.aBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter1)

    def a_the_second_bttln_mod_button_was_clicked(self):

        if self.aBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.aBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdSecondBattalionCostSetText = self.aBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter1)

    def a_the_third_bttln_mod_button_was_clicked(self):

        if self.aBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.aBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdThirdBattalionCostSetText = self.aBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter1)

    def a_the_fourth_bttln_mod_button_was_clicked(self):

        if self.aBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.aBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdFourthBattalionCostSetText = self.aBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter1)

    def a_the_add_bttln_mod_button_was_clicked(self):

        if self.aBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.aBrgdAdditionalBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.aBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.presenter1)

    # -------------------------------------------------------------------------------------------------------------------
    # описание кнопок второй бригады
    def bBrgdCommanderCostView(self, index):
        value = self.presenter2.rusLineInfantryBrigadeCmndrsCost(index)
        self.bBrgdCmndrCost.setText(str(value))
        self.bBrgdTotalCostView()

    def bBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        # создаем универсальную ссылку для стоимости первого батальона
        # отправляем индекс в презентер для передачи в модель чтобы поместить соотетствующий батальон на его место в бригаде
        order_number = 0  # порядковое место в бригаде
        # индекс выбранного баталльона из списка
        self.presenter2.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)
        # отправляем запрос стоимости батальона стоящего на соответствующем месте в бригаде
        value = self.presenter2.rusLineInfantryBrigadeBttlnCost(order_number)
        # записываем в соответствующее поле значение стоимости батальона
        self.bBrgdFirstBattalionCost.setText(str(value))

        self.bBrgdTotalCostView()

    def bBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        order_number = 1
        self.presenter2.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter2.rusLineInfantryBrigadeBttlnCost(order_number)
        self.bBrgdSecondBattalionCost.setText(str(value))
        self.bBrgdTotalCostView()

    def bBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        order_number = 2
        self.presenter2.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter2.rusLineInfantryBrigadeBttlnCost(order_number)
        self.bBrgdThirdBattalionCost.setText(str(value))
        self.bBrgdTotalCostView()

    def bBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        order_number = 3
        self.presenter2.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter2.rusLineInfantryBrigadeBttlnCost(order_number)
        self.bBrgdFourthBattalionCost.setText(str(value))
        self.bBrgdTotalCostView()

    def bBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        order_number = 4
        self.presenter2.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter2.rusLineInfantryBrigadeBttlnCost(order_number)
        self.bBrgdAddBattalionCost.setText(str(value))
        self.bBrgdTotalCostView()

    def bBrgdTotalCostView(self):
        total_cost = self.presenter2.rusLineInfantryBrigadeCmndrsCost(self.bBrgdCmndr.currentIndex()) + \
                     sum(self.presenter2.rusLineInfantryBrigadeBttlnCost(i) for i in range(5))

        self.bBrgdTotalCost.setText(str(total_cost))
        self.corpsTotalCostView()
    def b_the_first_bttln_mod_button_was_clicked(self):

        if self.bBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.bBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdFirstBattalionCostSetText = self.bBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter2)


    def b_the_second_bttln_mod_button_was_clicked(self):

        if self.bBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.bBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdSecondBattalionCostSetText = self.bBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter2)

    def b_the_third_bttln_mod_button_was_clicked(self):

        if self.bBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.bBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdThirdBattalionCostSetText = self.bBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter2)

    def b_the_fourth_bttln_mod_button_was_clicked(self):

        if self.bBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.bBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdFourthBattalionCostSetText = self.bBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter2)

    def b_the_add_bttln_mod_button_was_clicked(self):

        if self.bBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.bBrgdAdditionalBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdFifthBattalionCostSetText = self.bBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter2)

#-------------------------------------------------------------------------------------------------------------------
    def cBrgdCommanderCostView(self, index):
        value = self.presenter3.rusLineInfantryBrigadeCmndrsCost(index)
        self.cBrgdCmndrCost.setText(str(value))
        self.cBrgdTotalCostView()

    def cBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        # отправляем индекс в презентер для передачи в модель чтобы поместить соотетствующий батальон на его место в бригаде
        order_number = 0  # порядковое место в бригаде
        # индекс выбранного баталльона из списка
        self.presenter3.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)
        # отправляем запрос стоимости батальона стоящего на соответствующем месте в бригаде
        value = self.presenter3.rusLineInfantryBrigadeBttlnCost(order_number)
        # записываем в соответствующее поле значение стоимости батальона
        self.cBrgdFirstBattalionCost.setText(str(value))

        self.cBrgdTotalCostView()

    def cBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        order_number = 1
        self.presenter3.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter3.rusLineInfantryBrigadeBttlnCost(order_number)
        self.cBrgdSecondBattalionCost.setText(str(value))
        self.cBrgdTotalCostView()

    def cBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        order_number = 2
        self.presenter3.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter3.rusLineInfantryBrigadeBttlnCost(order_number)
        self.cBrgdThirdBattalionCost.setText(str(value))
        self.cBrgdTotalCostView()

    def cBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        order_number = 3
        self.presenter3.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter3.rusLineInfantryBrigadeBttlnCost(order_number)
        self.cBrgdFourthBattalionCost.setText(str(value))
        self.cBrgdTotalCostView()

    def cBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        order_number = 4
        self.presenter3.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)

        value = self.presenter3.rusLineInfantryBrigadeBttlnCost(order_number)
        self.cBrgdAddBattalionCost.setText(str(value))
        self.cBrgdTotalCostView()

    def cBrgdTotalCostView(self):
        total_cost = self.presenter3.rusLineInfantryBrigadeCmndrsCost(self.cBrgdCmndr.currentIndex()) + \
                     sum(self.presenter3.rusLineInfantryBrigadeBttlnCost(i) for i in range(5))

        self.cBrgdTotalCost.setText(str(total_cost))
        self.corpsTotalCostView()
    def c_the_first_bttln_mod_button_was_clicked(self):

        if self.cBrgdFirstBattalion.currentIndex() != 0:

            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.cBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdFirstBattalionCostSetText = self.cBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter3)

    def c_the_second_bttln_mod_button_was_clicked(self):

        if self.cBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.cBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdSecondBattalionCostSetText = self.cBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter3)

    def c_the_third_bttln_mod_button_was_clicked(self):

        if self.cBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.cBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdThirdBattalionCostSetText = self.cBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter3)

    def c_the_fourth_bttln_mod_button_was_clicked(self):

        if self.cBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.cBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.brgdFourthBattalionCostSetText = self.cBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView

            self.bttln_mod_button_was_clicked(battalion_order, self.presenter3)

    def c_the_add_bttln_mod_button_was_clicked(self):

        if self.cBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.cBrgdAdditionalBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.cBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.presenter3)

    # -------------------------------------------------------------------------------------------------------------------


    def bttln_mod_button_was_clicked(self, battalion_order, presenter):

        self.presenter = presenter
        self.bonus_window = BonusWindow()
        self.bonus_window.setWindowTitle(battalion_order)

        self.bonus1 = ""
        self.bonus2 = ""
        self.bonus3 = ""

        # создаем временную переменную стоимости батальона , для отображения в окне бонусов
        self.temporary_bonus_cost = self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)
        # создаем временный список бонусов батальона
        self.temporary_bonus_list = self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number).copy()

        self.bonus_window.name.setText(str(self.presenter.rusLineInfantryBrigadeBttlnName(self.order_number)))
        self.bonus_window.cost.setText(str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))

        # заполняем названия бонусов
        self.bonus_window.bonus1.setText(self.presenter.rusLineInfantryBrigadeBonusNameList(0))
        self.bonus_window.bonus2.setText(self.presenter.rusLineInfantryBrigadeBonusNameList(1))
        self.bonus_window.bonus3.setText(self.presenter.rusLineInfantryBrigadeBonusNameList(2))

        # если имя выбранного батальона не соответствует списку имен для данного бонуса, то выключаем этот пункт меню
        if self.presenter.rusLineInfantryBrigadeBttlnName(self.order_number) not in \
                self.presenter.rusLineInfantryBrigadeBonusToBattalion(
                    self.presenter.rusLineInfantryBrigadeBonusNameList(0)):
            self.bonus_window.bonus1.close()
            self.bonus_window.checkBox_1.close()

        if self.presenter.rusLineInfantryBrigadeBttlnName(self.order_number) not in \
                self.presenter.rusLineInfantryBrigadeBonusToBattalion(
                    self.presenter.rusLineInfantryBrigadeBonusNameList(1)):
            self.bonus_window.bonus2.close()
            self.bonus_window.checkBox_2.close()

        if self.presenter.rusLineInfantryBrigadeBttlnName(self.order_number) not in \
                self.presenter.rusLineInfantryBrigadeBonusToBattalion(
                    self.presenter.rusLineInfantryBrigadeBonusNameList(2)):
            self.bonus_window.bonus3.close()
            self.bonus_window.checkBox_3.close()

        # вводим проверку на наличие первого бонуса у батальона. Если есть то статус чекбокса - нажат
        if self.presenter.rusLineInfantryBrigadeBonusNameList(0) in self.presenter.rusLineInfantryBrigadeBttlnBonusList(
                self.order_number):
            self.bonus_window.checkBox_1.setChecked(True)
        self.bonus_window.checkBox_1.stateChanged.connect(self.checkBox1_Action)
        # вводим проверку на наличие второго бонуса у батальона. Если есть то статус чекбокса - нажат
        if self.presenter.rusLineInfantryBrigadeBonusNameList(1) in self.presenter.rusLineInfantryBrigadeBttlnBonusList(
                self.order_number):
            self.bonus_window.checkBox_2.setChecked(True)
        self.bonus_window.checkBox_2.stateChanged.connect(self.checkBox2_Action)
        # вводим проверку на наличие второго бонуса у батальона. Если есть то статус чекбокса - нажат
        if self.presenter.rusLineInfantryBrigadeBonusNameList(2) in self.presenter.rusLineInfantryBrigadeBttlnBonusList(
                self.order_number):
            self.bonus_window.checkBox_3.setChecked(True)
        self.bonus_window.checkBox_3.stateChanged.connect(self.checkBox3_Action)

        self.bonus_window.ok_button.clicked.connect(self.ok_button_was_clicked)

        self.bonus_window.cancel_button.clicked.connect(self.cancel_button_was_clicked)
        self.bonus_window.show()

    def ok_button_was_clicked(self):
        # проверка - не переключил ли пользователь отряд , пока открыто окно выбора бонусов
        if self.current_bttln_index != 0:
            # проверка если выбранный бонус не пуст то тогда применяются свойства бонууса.
            if self.bonus1 != "":
                # проверяем если чекбокс был нажат то добавляем свойста, если отжат , то удаляем свойства и стоимость
                if self.bonus_window.checkBox_1.isChecked():
                    # проверяем, если такой такого юонуса еще нет то добавляем
                    if self.presenter.rusLineInfantryBrigadeBonusNameList(
                            0) not in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusAdd(self.bonus1, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus1_cost, self.order_number)
                else:
                    # проверяем, если такой бонус есть то удаляем
                    if self.presenter.rusLineInfantryBrigadeBonusNameList(
                            0) in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusDel(self.bonus1, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus1_cost * (-1),
                                                                               self.order_number)
            # проверка если выбранный бонус 2 не пуст то тогда применяются свойства бонууса.
            if self.bonus2 != "":
                # проверяем если чекбокс был нажат то добавляем свойста, если отжат , то удаляем свойства и стоимость
                if self.bonus_window.checkBox_2.isChecked():
                    # проверяем, если такой такого юонуса еще нет то добавляем
                    if self.presenter.rusLineInfantryBrigadeBonusNameList(
                            1) not in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusAdd(self.bonus2, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus2_cost, self.order_number)
                else:
                    # проверяем, если такой бонус есть то удаляем
                    if self.presenter.rusLineInfantryBrigadeBonusNameList(
                            1) in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusDel(self.bonus2, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus2_cost * (-1),
                                                                               self.order_number)
                    # проверка если выбранный бонус 3 не пуст то тогда применяются свойства бонууса.
            if self.bonus3 != "":
                # проверяем если чекбокс был нажат то добавляем свойста, если отжат , то удаляем свойства и стоимость
                if self.bonus_window.checkBox_3.isChecked():
                    # проверяем, если такой такого юонуса еще нет то добавляем
                    if self.presenter.rusLineInfantryBrigadeBonusNameList(
                            2) not in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusAdd(self.bonus3, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus3_cost, self.order_number)
                else:
                    # проверяем, если такой бонус есть то удаляем
                    if self.presenter.rusLineInfantryBrigadeBonusNameList(
                            2) in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusDel(self.bonus3, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus3_cost * (-1),
                                                                               self.order_number)
            match self.order_number:
                case 0:
                    self.brgdFirstBattalionCostSetText(
                        str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))
                case 1:
                    self.brgdSecondBattalionCostSetText(
                        str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))
                case 2:
                    self.brgdThirdBattalionCostSetText(
                        str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))
                case 3:
                    self.brgdFourthBattalionCostSetText(
                        str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))
                case 4:
                    self.brgdFifthBattalionCostSetText(
                        str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))

            # и обновляем полную стоимость бригады
            self.brgdTotalCostView()

            self.bonus_window.close()
        else:
            self.cancel_button_was_clicked()

    def cancel_button_was_clicked(self):
        self.bonus_window.close()

    def checkBox1_Action(self):
        self.bonus1 = self.presenter.rusLineInfantryBrigadeBonusNameList(0)
        self.bonus1_cost = self.presenter.rusLineInfantryBrigadeBonusCostList(0)
        # изменение величины бонуса для двух батальонов егерей
        if self.presenter.rusLineInfantryBrigadeBttlnName(self.order_number) == "Jager 2 battalions":
            self.bonus1_cost *= 2

        # проверка если чекбокс нажат и такого бонуса еще нет в списке бонусов батальона, то в окне отображения бонусов показывается стоимость с бонусом ()
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс нажат и такой бонус уже есть, то показывается стоимость взятая из обьекта батальон
        if self.bonus_window.checkBox_1.isChecked():
            if self.presenter.rusLineInfantryBrigadeBonusNameList(0) not in self.temporary_bonus_list:
                self.temporary_bonus_cost += self.bonus1_cost  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list[
                    self.presenter.rusLineInfantryBrigadeBonusNameList(0)] = None  # вносим бонус во временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
        # проверка если чекбокс отжат и такой бонус есть в списке бонусов батальона, то в окне отображения бонусов показывается стоимость за вычетом бонуса
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс отжат  и такого бонуса нет, то показывается стоимость взятая из обьекта батальон
        else:
            if self.presenter.rusLineInfantryBrigadeBonusNameList(0) in self.temporary_bonus_list:
                self.temporary_bonus_cost -= self.bonus1_cost  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list[
                    self.presenter.rusLineInfantryBrigadeBonusNameList(0)]  # удаляем бонус из временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))

    def checkBox2_Action(self):
        self.bonus2 = self.presenter.rusLineInfantryBrigadeBonusNameList(1)
        self.bonus2_cost = self.presenter.rusLineInfantryBrigadeBonusCostList(1)
        # изменение величины бонуса для двух батальонов егерей
        if self.presenter.rusLineInfantryBrigadeBttlnName(self.order_number) == "Jager 2 battalions":
            self.bonus2_cost *= 2

        if self.bonus_window.checkBox_2.isChecked():
            if self.presenter.rusLineInfantryBrigadeBonusNameList(1) not in self.temporary_bonus_list:

                self.temporary_bonus_cost += self.bonus2_cost  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list[
                    self.presenter.rusLineInfantryBrigadeBonusNameList(1)] = None  # вносим бонус во временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
        else:
            if self.presenter.rusLineInfantryBrigadeBonusNameList(1) in self.temporary_bonus_list:

                self.temporary_bonus_cost -= self.bonus2_cost  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list[
                    self.presenter.rusLineInfantryBrigadeBonusNameList(1)]  # удаляем бонус из временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))

    def checkBox3_Action(self):
        self.bonus3 = self.presenter.rusLineInfantryBrigadeBonusNameList(2)
        self.bonus3_cost = self.presenter.rusLineInfantryBrigadeBonusCostList(2)

        if self.bonus_window.checkBox_3.isChecked():
            if self.presenter.rusLineInfantryBrigadeBonusNameList(2) not in self.temporary_bonus_list:

                self.temporary_bonus_cost += self.bonus3_cost  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list[
                    self.presenter.rusLineInfantryBrigadeBonusNameList(2)] = None  # вносим бонус во временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
        else:
            if self.presenter.rusLineInfantryBrigadeBonusNameList(2) in self.temporary_bonus_list:

                self.temporary_bonus_cost -= self.bonus3_cost  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list[
                    self.presenter.rusLineInfantryBrigadeBonusNameList(2)]  # удаляем бонус из временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
