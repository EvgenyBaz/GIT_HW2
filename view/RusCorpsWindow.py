from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout
import sys

from presenter.presenter import Presenter
from view.RusCorpsGuiWindow import Ui_RusCorpsWindow
from view.BonusWindow import BonusWindow

from view.brigades.infantry_brigade_view import *
from view.brigades.jager_brigade_view import *


class RusCorpsWindow(QtWidgets.QMainWindow, Ui_RusCorpsWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(RusCorpsWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.country = "Rus" # определяем страну
        self.presenter = Presenter(self.country)

        self.generalName.currentIndexChanged.connect(self.corpsCommanderCostView)

        self.a_brigade_number = 0  # номер бригады попорядку

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

        self.b_brigade_number = 1

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

        self.c_brigade_number = 2

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

        self.jgr_brigade_number = 3

        self.JgrBrgdCmndr.currentIndexChanged.connect(self.jgrBrgdCommanderCostView)
        self.JgrBrgdFirstBattalion.currentIndexChanged.connect(self.jgrBrgd1stBttlnCostView)
        self.JgrBrgdSecondBattalion.currentIndexChanged.connect(self.jgrBrgd2ndBttlnCostView)
        self.JgrBrgdThirdBattalion.currentIndexChanged.connect(self.jgrBrgd3rdBttlnCostView)
        self.JgrBrgdFourthBattalion.currentIndexChanged.connect(self.jgrBrgd4thBttlnCostView)
        self.JgrBrgdFifthBattalion.currentIndexChanged.connect(self.jgrBrgd5thBttlnCostView)
        self.JgrBrgdSixthBattalion.currentIndexChanged.connect(self.jgrBrgd6thBttlnCostView)
        self.JgrBrgdAdditional1Battalion.currentIndexChanged.connect(self.jgrBrgdAdd1BttlnCostView)
        self.JgrBrgdAdditional2Battalion.currentIndexChanged.connect(self.jgrBrgdAdd2BttlnCostView)

        self.JgrBrFirstBttlnModPushButton.clicked.connect(self.jgr_the_first_bttln_mod_button_was_clicked)
        self.JgrBrSecondBttlnModPushButton.clicked.connect(self.jgr_the_second_bttln_mod_button_was_clicked)
        self.JgrBrThirdBttlnModPushButton.clicked.connect(self.jgr_the_third_bttln_mod_button_was_clicked)
        self.JgrBrFourthBttlnModPushButton.clicked.connect(self.jgr_the_fourth_bttln_mod_button_was_clicked)
        self.JgrBrFifthBttlnModPushButton.clicked.connect(self.jgr_the_fifth_bttln_mod_button_was_clicked)
        self.JgrBrSixthBttlnModPushButton.clicked.connect(self.jgr_the_sixth_bttln_mod_button_was_clicked)

#заполняем список имен командиров корпуса
    def corps_cmndrs_list(self):
        cmndrs_list = self.presenter.CorpsCmndrsNamesList()
        for cmndrName in cmndrs_list:
            self.generalName.addItem(cmndrName)

    def corpsCommanderCostView(self, index):
        value = self.presenter.CorpsCmndrsCost(index)
        self.generalCost.setText(str(value))
        self.corpsTotalCostView()

    def corpsTotalCostView(self):
        total_cost =int(self.generalCost.text())+int(self.aBrgdTotalCost.text()) + int(self.bBrgdTotalCost.text()) + int(self.cBrgdTotalCost.text())+ int(self.JgrBrgdTotalCost.text())
        self.corpsTotalCost.setText(str(total_cost))
#------------------------------------------------------------------------------------------------------------------
    def brgdCommanderCostView(self, index, brigade_number, brgdCmndrCost):
        value = self.presenter.BrigadeCmndrsCost(index, brigade_number)
        brgdCmndrCost.setText(str(value))

    def brgdBttlnCostView(self, bttln_choosen_from_list, brigade_number, brgdBattalionCost,
                          brgdTotalCostView, order_number):
        # отправляем индекс в презентер для передачи в модель чтобы поместить соотетствующий батальон на его место в бригаде
        # order_number =  порядковое место в бригаде
        # индекс выбранного баталльона из списка
        self.presenter.BrigadeBttlnChoosen(order_number, bttln_choosen_from_list, brigade_number)
        # отправляем запрос стоимости батальона стоящего на соответствующем месте в бригаде
        value = self.presenter.BrigadeBttlnCost(order_number, brigade_number)
        # записываем в соответствующее поле значение стоимости батальона
        brgdBattalionCost.setText(str(value))
        brgdTotalCostView()

# -------------------------------------------------------------------------------------------------------------------
    def a_brigade_bttln_Lists(self):
        inf_brigade_bttln_Lists(self.a_brigade_number, self.presenter, self.aBrgdCmndr, self.aBrgdFirstBattalion,
                              self.aBrgdSecondBattalion, self.aBrgdThirdBattalion, self.aBrgdFourthBattalion,
                              self.aBrgdAdditionalBattalion)

    def aBrgdCommanderCostView(self, index):
        self.brgdCommanderCostView(index,  self.a_brigade_number, self.aBrgdCmndrCost)
        self.aBrgdTotalCostView()

    def aBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list,  self.a_brigade_number,
                              self.aBrgdFirstBattalionCost, self.aBrgdTotalCostView, 0)

    def aBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                              self.aBrgdSecondBattalionCost, self.aBrgdTotalCostView, 1)

    def aBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                              self.aBrgdThirdBattalionCost, self.aBrgdTotalCostView, 2)

    def aBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list,  self.a_brigade_number,
                              self.aBrgdFourthBattalionCost, self.aBrgdTotalCostView, 3)

    def aBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                              self.aBrgdAddBattalionCost, self.aBrgdTotalCostView, 4)

    def aBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.aBrgdCmndr.currentIndex(), self.a_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.a_brigade_number) for i in range(5))

        self.aBrgdTotalCost.setText(str(total_cost))
        self.corpsTotalCostView()

    def a_the_first_bttln_mod_button_was_clicked(self):
        if self.aBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.aBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFirstBattalionCostSetText = self.aBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number)

    def a_the_second_bttln_mod_button_was_clicked(self):
        if self.aBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.aBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSecondBattalionCostSetText = self.aBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number)

    def a_the_third_bttln_mod_button_was_clicked(self):
        if self.aBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.aBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdThirdBattalionCostSetText = self.aBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number)

    def a_the_fourth_bttln_mod_button_was_clicked(self):
        if self.aBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.aBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFourthBattalionCostSetText = self.aBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number)

    def a_the_add_bttln_mod_button_was_clicked(self):
        if self.aBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.aBrgdAdditionalBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.aBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number)

    # -------------------------------------------------------------------------------------------------------------------
    def b_brigade_bttln_Lists(self):
        inf_brigade_bttln_Lists(self.b_brigade_number, self.presenter, self.bBrgdCmndr, self.bBrgdFirstBattalion,
                              self.bBrgdSecondBattalion, self.bBrgdThirdBattalion, self.bBrgdFourthBattalion,
                              self.bBrgdAdditionalBattalion)
    # описание кнопок второй бригады
    def bBrgdCommanderCostView(self, index):
        self.brgdCommanderCostView(index, self.b_brigade_number, self.bBrgdCmndrCost)
        self.bBrgdTotalCostView()

    def bBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                              self.bBrgdFirstBattalionCost, self.bBrgdTotalCostView, 0)

    def bBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                              self.bBrgdSecondBattalionCost, self.bBrgdTotalCostView, 1)

    def bBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                              self.bBrgdThirdBattalionCost, self.bBrgdTotalCostView, 2)

    def bBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                              self.bBrgdFourthBattalionCost, self.bBrgdTotalCostView, 3)

    def bBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                              self.bBrgdAddBattalionCost, self.bBrgdTotalCostView, 4)

    def bBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.bBrgdCmndr.currentIndex(), self.b_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.b_brigade_number) for i in range(5))

        self.bBrgdTotalCost.setText(str(total_cost))
        self.corpsTotalCostView()

    def b_the_first_bttln_mod_button_was_clicked(self):

        if self.bBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.bBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFirstBattalionCostSetText = self.bBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number)

    def b_the_second_bttln_mod_button_was_clicked(self):

        if self.bBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.bBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSecondBattalionCostSetText = self.bBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number)

    def b_the_third_bttln_mod_button_was_clicked(self):

        if self.bBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.bBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdThirdBattalionCostSetText = self.bBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number)

    def b_the_fourth_bttln_mod_button_was_clicked(self):

        if self.bBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.bBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFourthBattalionCostSetText = self.bBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number)

    def b_the_add_bttln_mod_button_was_clicked(self):

        if self.bBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.bBrgdAdditionalBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.bBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number)

# -------------------------------------------------------------------------------------------------------------------

    def c_brigade_bttln_Lists(self):
        inf_brigade_bttln_Lists(self.c_brigade_number, self.presenter, self.cBrgdCmndr, self.cBrgdFirstBattalion,
                              self.cBrgdSecondBattalion, self.cBrgdThirdBattalion, self.cBrgdFourthBattalion,
                              self.cBrgdAdditionalBattalion)

    def cBrgdCommanderCostView(self, index):
        self.brgdCommanderCostView(index, self.c_brigade_number, self.cBrgdCmndrCost)
        self.cBrgdTotalCostView()

    def cBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                              self.cBrgdFirstBattalionCost, self.cBrgdTotalCostView, 0)

    def cBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                              self.cBrgdSecondBattalionCost, self.cBrgdTotalCostView, 1)

    def cBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                              self.cBrgdThirdBattalionCost, self.cBrgdTotalCostView, 2)

    def cBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                              self.cBrgdFourthBattalionCost, self.cBrgdTotalCostView, 3)

    def cBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                              self.cBrgdAddBattalionCost, self.cBrgdTotalCostView, 4)

    def cBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.cBrgdCmndr.currentIndex(), self.c_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.c_brigade_number) for i in range(5))

        self.cBrgdTotalCost.setText(str(total_cost))
        self.corpsTotalCostView()
    def c_the_first_bttln_mod_button_was_clicked(self):

        if self.cBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.cBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFirstBattalionCostSetText = self.cBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number)

    def c_the_second_bttln_mod_button_was_clicked(self):

        if self.cBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.cBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSecondBattalionCostSetText = self.cBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number)

    def c_the_third_bttln_mod_button_was_clicked(self):

        if self.cBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.cBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdThirdBattalionCostSetText = self.cBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number)

    def c_the_fourth_bttln_mod_button_was_clicked(self):

        if self.cBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.cBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFourthBattalionCostSetText = self.cBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number)

    def c_the_add_bttln_mod_button_was_clicked(self):

        if self.cBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.cBrgdAdditionalBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.cBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number)

    # -------------------------------------------------------------------------------------------------------------------
    def jgr_brigade_bttln_Lists(self):
        jgr_brigade_bttln_Lists(self.jgr_brigade_number, self.presenter, self.JgrBrgdCmndr, self.JgrBrgdFirstBattalion,
                              self.JgrBrgdSecondBattalion, self.JgrBrgdThirdBattalion, self.JgrBrgdFourthBattalion,
                              self.JgrBrgdFifthBattalion, self.JgrBrgdSixthBattalion, self.JgrBrgdAdditional1Battalion,
                              self.JgrBrgdAdditional2Battalion)
    def jgrBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.jgr_brigade_number)
        self.JgrBrgdCmndrCost.setText(str(value))
        self.jgrBrgdTotalCostView()

    def jgrBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                              self.JgrBrgdFirstBattalionCost, self.jgrBrgdTotalCostView, 0)

    def jgrBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                              self.JgrBrgdSecondBattalionCost, self.jgrBrgdTotalCostView, 1)

    def jgrBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                              self.JgrBrgdThirdBattalionCost, self.jgrBrgdTotalCostView, 2)

    def jgrBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                              self.JgrBrgdFourthBattalionCost, self.jgrBrgdTotalCostView, 3)

    def jgrBrgd5thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                              self.JgrBrgdFifthBattalionCost, self.jgrBrgdTotalCostView, 4)

    def jgrBrgd6thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                              self.JgrBrgdSixthBattalionCost, self.jgrBrgdTotalCostView, 5)

    def jgrBrgdAdd1BttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                              self.JgrBrgdAdd1BattalionCost, self.jgrBrgdTotalCostView, 6)

    def jgrBrgdAdd2BttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                              self.JgrBrgdAdd2BattalionCost, self.jgrBrgdTotalCostView, 7)

    def jgrBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.JgrBrgdCmndr.currentIndex(),
                                                                     self.jgr_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.jgr_brigade_number) for i in range(8))

        self.JgrBrgdTotalCost.setText(str(total_cost))
        self.corpsTotalCostView()

    def jgr_the_first_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.JgrBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFirstBattalionCostSetText = self.JgrBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number)

    def jgr_the_second_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.JgrBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSecondBattalionCostSetText = self.JgrBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number)

    def jgr_the_third_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.JgrBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdThirdBattalionCostSetText = self.JgrBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number)

    def jgr_the_fourth_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.JgrBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFourthBattalionCostSetText = self.JgrBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number)

    def jgr_the_fifth_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdFifthBattalion.currentIndex() != 0:
            battalion_order = "Fifth Battalion"
            self.order_number = 4  # четвертый по порядку батальон
            self.current_bttln_index = self.JgrBrgdFifthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.JgrBrgdFifthBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number)
    def jgr_the_sixth_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdSixthBattalion.currentIndex() != 0:
            battalion_order = "Sixth Battalion"
            self.order_number = 5  # четвертый по порядку батальон
            self.current_bttln_index = self.JgrBrgdSixthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSixthBattalionCostSetText = self.JgrBrgdSixthBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number)
    # -------------------------------------------------------------------------------------------------------------------

    def bttln_mod_button_was_clicked(self, battalion_order, brigade_number):

        self.brigade_number = brigade_number
        self.bonus_window = BonusWindow()
        self.bonus_window.setWindowTitle(battalion_order)

        self.bonus1 = ""
        self.bonus2 = ""
        self.bonus3 = ""

        # создаем временную переменную стоимости батальона , для отображения в окне бонусов
        self.temporary_bonus_cost = self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)
        # создаем временный список бонусов батальона
        self.temporary_bonus_list = self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number).copy()

        self.bonus_window.name.setText(str(self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number)))
        self.bonus_window.cost.setText(str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))

        # заполняем названия бонусов
        self.bonus_window.bonus1.setText(self.presenter.BrigadeBonusNameList(0, self.brigade_number))
        self.bonus_window.bonus2.setText(self.presenter.BrigadeBonusNameList(1, self.brigade_number))
        self.bonus_window.bonus3.setText(self.presenter.BrigadeBonusNameList(2, self.brigade_number))

        # если имя выбранного батальона не соответствует списку имен для данного бонуса, то выключаем этот пункт меню
        if self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number) not in \
                self.presenter.BrigadeBonusToBattalion(
                    self.presenter.BrigadeBonusNameList(0, self.brigade_number), self.brigade_number):
            self.bonus_window.bonus1.close()
            self.bonus_window.checkBox_1.close()

        if self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number) not in \
                self.presenter.BrigadeBonusToBattalion(
                    self.presenter.BrigadeBonusNameList(1, self.brigade_number), self.brigade_number):
            self.bonus_window.bonus2.close()
            self.bonus_window.checkBox_2.close()

        if self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number) not in \
                self.presenter.BrigadeBonusToBattalion(
                    self.presenter.BrigadeBonusNameList(2, self.brigade_number), self.brigade_number):
            self.bonus_window.bonus3.close()
            self.bonus_window.checkBox_3.close()

        # вводим проверку на наличие первого бонуса у батальона. Если есть то статус чекбокса - нажат
        if self.presenter.BrigadeBonusNameList(0, self.brigade_number) in self.presenter.BrigadeBttlnBonusList(
                self.order_number, self.brigade_number):
            self.bonus_window.checkBox_1.setChecked(True)
        self.bonus_window.checkBox_1.stateChanged.connect(self.checkBox1_Action)
        # вводим проверку на наличие второго бонуса у батальона. Если есть то статус чекбокса - нажат
        if self.presenter.BrigadeBonusNameList(1, self.brigade_number) in self.presenter.BrigadeBttlnBonusList(
                self.order_number, self.brigade_number):
            self.bonus_window.checkBox_2.setChecked(True)
        self.bonus_window.checkBox_2.stateChanged.connect(self.checkBox2_Action)
        # вводим проверку на наличие второго бонуса у батальона. Если есть то статус чекбокса - нажат
        if self.presenter.BrigadeBonusNameList(2, self.brigade_number) in self.presenter.BrigadeBttlnBonusList(
                self.order_number, self.brigade_number):
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
                    if self.presenter.BrigadeBonusNameList(
                            0, self.brigade_number) not in self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number):
                        self.presenter.BrigadeBttlnBonusAdd(self.bonus1, self.order_number, self.brigade_number)
                        self.presenter.BrigadeBttlnBonusCostAdd(self.bonus1_cost, self.order_number, self.brigade_number)
                else:
                    # проверяем, если такой бонус есть то удаляем
                    if self.presenter.BrigadeBonusNameList(
                            0, self.brigade_number) in self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number):
                        self.presenter.BrigadeBttlnBonusDel(self.bonus1, self.order_number, self.brigade_number)
                        self.presenter.BrigadeBttlnBonusCostAdd(self.bonus1_cost * (-1),
                                                                               self.order_number, self.brigade_number)
            # проверка если выбранный бонус 2 не пуст то тогда применяются свойства бонууса.
            if self.bonus2 != "":
                # проверяем если чекбокс был нажат то добавляем свойста, если отжат , то удаляем свойства и стоимость
                if self.bonus_window.checkBox_2.isChecked():
                    # проверяем, если такой такого юонуса еще нет то добавляем
                    if self.presenter.BrigadeBonusNameList(
                            1, self.brigade_number) not in self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number):
                        self.presenter.BrigadeBttlnBonusAdd(self.bonus2, self.order_number, self.brigade_number)
                        self.presenter.BrigadeBttlnBonusCostAdd(self.bonus2_cost, self.order_number, self.brigade_number)
                else:
                    # проверяем, если такой бонус есть то удаляем
                    if self.presenter.BrigadeBonusNameList(
                            1, self.brigade_number) in self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number):
                        self.presenter.BrigadeBttlnBonusDel(self.bonus2, self.order_number, self.brigade_number)
                        self.presenter.BrigadeBttlnBonusCostAdd(self.bonus2_cost * (-1),
                                                                               self.order_number, self.brigade_number)
                    # проверка если выбранный бонус 3 не пуст то тогда применяются свойства бонууса.
            if self.bonus3 != "":
                # проверяем если чекбокс был нажат то добавляем свойста, если отжат , то удаляем свойства и стоимость
                if self.bonus_window.checkBox_3.isChecked():
                    # проверяем, если такой такого юонуса еще нет то добавляем
                    if self.presenter.BrigadeBonusNameList(
                            2, self.brigade_number) not in self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number):
                        self.presenter.BrigadeBttlnBonusAdd(self.bonus3, self.order_number, self.brigade_number)
                        self.presenter.BrigadeBttlnBonusCostAdd(self.bonus3_cost, self.order_number, self.brigade_number)
                else:
                    # проверяем, если такой бонус есть то удаляем
                    if self.presenter.BrigadeBonusNameList(
                            2, self.brigade_number) in self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number):
                        self.presenter.BrigadeBttlnBonusDel(self.bonus3, self.order_number, self.brigade_number)
                        self.presenter.BrigadeBttlnBonusCostAdd(self.bonus3_cost * (-1),
                                                                               self.order_number, self.brigade_number)
            match self.order_number:
                case 0:
                    self.brgdFirstBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 1:
                    self.brgdSecondBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 2:
                    self.brgdThirdBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 3:
                    self.brgdFourthBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 4:
                    self.brgdFifthBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 5:
                    self.brgdSixthBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))

            # и обновляем полную стоимость бригады
            self.brgdTotalCostView()

            self.bonus_window.close()
        else:
            self.cancel_button_was_clicked()

    def cancel_button_was_clicked(self):
        self.bonus_window.close()

    def checkBox1_Action(self):
        self.bonus1 = self.presenter.BrigadeBonusNameList(0, self.brigade_number)
        self.bonus1_cost = self.presenter.BrigadeBonusCostList(0, self.brigade_number)
        # изменение величины бонуса для двух батальонов егерей
        if self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number) == "Jager 2 battalions":
            self.bonus1_cost *= 2

        # проверка если чекбокс нажат и такого бонуса еще нет в списке бонусов батальона, то в окне отображения бонусов показывается стоимость с бонусом ()
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс нажат и такой бонус уже есть, то показывается стоимость взятая из обьекта батальон
        if self.bonus_window.checkBox_1.isChecked():
            if self.presenter.BrigadeBonusNameList(0, self.brigade_number) not in self.temporary_bonus_list:
                self.temporary_bonus_cost += self.bonus1_cost  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list[
                    self.presenter.BrigadeBonusNameList(0, self.brigade_number)] = None  # вносим бонус во временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
        # проверка если чекбокс отжат и такой бонус есть в списке бонусов батальона, то в окне отображения бонусов показывается стоимость за вычетом бонуса
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс отжат  и такого бонуса нет, то показывается стоимость взятая из обьекта батальон
        else:
            if self.presenter.BrigadeBonusNameList(0, self.brigade_number) in self.temporary_bonus_list:
                self.temporary_bonus_cost -= self.bonus1_cost  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list[
                    self.presenter.BrigadeBonusNameList(0, self.brigade_number)]  # удаляем бонус из временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))

    def checkBox2_Action(self):
        self.bonus2 = self.presenter.BrigadeBonusNameList(1, self.brigade_number)
        self.bonus2_cost = self.presenter.BrigadeBonusCostList(1, self.brigade_number)
        # изменение величины бонуса для двух батальонов егерей
        if self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number) == "Jager 2 battalions":
            self.bonus2_cost *= 2

        if self.bonus_window.checkBox_2.isChecked():
            if self.presenter.BrigadeBonusNameList(1, self.brigade_number) not in self.temporary_bonus_list:

                self.temporary_bonus_cost += self.bonus2_cost  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list[
                    self.presenter.BrigadeBonusNameList(1, self.brigade_number)] = None  # вносим бонус во временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
        else:
            if self.presenter.BrigadeBonusNameList(1, self.brigade_number) in self.temporary_bonus_list:

                self.temporary_bonus_cost -= self.bonus2_cost  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list[
                    self.presenter.BrigadeBonusNameList(1, self.brigade_number)]  # удаляем бонус из временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))

    def checkBox3_Action(self):
        self.bonus3 = self.presenter.BrigadeBonusNameList(2, self.brigade_number)
        self.bonus3_cost = self.presenter.BrigadeBonusCostList(2, self.brigade_number)

        if self.bonus_window.checkBox_3.isChecked():
            if self.presenter.BrigadeBonusNameList(2, self.brigade_number) not in self.temporary_bonus_list:

                self.temporary_bonus_cost += self.bonus3_cost  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list[
                    self.presenter.BrigadeBonusNameList(2, self.brigade_number)] = None  # вносим бонус во временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
        else:
            if self.presenter.BrigadeBonusNameList(2, self.brigade_number) in self.temporary_bonus_list:

                self.temporary_bonus_cost -= self.bonus3_cost  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list[
                    self.presenter.BrigadeBonusNameList(2, self.brigade_number)]  # удаляем бонус из временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
