from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout
import sys

from presenter.presenter import Presenter
from view.RusDivisionGuiWindow import Ui_RusDivisionWindow
from view.BonusWindow import BonusWindow

from view.brigades.infantry_brigade_view import *
from view.brigades.jager_brigade_view import *
from view.brigades.combined_grenadier_brigade_view import *


class RusDivisionWindow(QtWidgets.QMainWindow, Ui_RusDivisionWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(RusDivisionWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.country = "Rus"  # определяем страну
        self.presenter = Presenter(self.country)

        self.generalName.currentIndexChanged.connect(self.divisionCommanderCostView)

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

        self.comb_grndr_brigade_number = 4

        self.CombGrndrBrgdCmndr.currentIndexChanged.connect(self.combGrndrBrgdCommanderCostView)
        self.CombGrndrBrgdFirstBattalion.currentIndexChanged.connect(self.combGrndrBrgd1stBttlnCostView)
        self.CombGrndrBrgdSecondBattalion.currentIndexChanged.connect(self.combGrndrBrgd2ndBttlnCostView)
        self.CombGrndrBrgdThirdBattalion.currentIndexChanged.connect(self.combGrndrBrgd3rdBttlnCostView)
        self.CombGrndrBrgdFourthBattalion.currentIndexChanged.connect(self.combGrndrBrgd4thBttlnCostView)
        self.CombGrndrBrgdFifthBattalion.currentIndexChanged.connect(self.combGrndrBrgd5thBttlnCostView)
        self.CombGrndrBrgdSixthBattalion.currentIndexChanged.connect(self.combGrndrBrgd6thBttlnCostView)
        self.CombGrndrBrgdSeventhBattalion.currentIndexChanged.connect(self.combGrndrBrgd7thBttlnCostView)

        self.CombGrndrBrFirstBttlnModPushButton.clicked.connect(self.comb_grndr_the_first_bttln_mod_button_was_clicked)
        self.CombGrndrBrSecondBttlnModPushButton.clicked.connect(self.comb_grndr_the_second_bttln_mod_button_was_clicked)
        self.CombGrndrBrThirdBttlnModPushButton.clicked.connect(self.comb_grndr_the_third_bttln_mod_button_was_clicked)
        self.CombGrndrBrFourthBttlnModPushButton.clicked.connect(self.comb_grndr_the_fourth_bttln_mod_button_was_clicked)
        self.CombGrndrBrFifthBttlnModPushButton.clicked.connect(self.comb_grndr_the_fifth_bttln_mod_button_was_clicked)
        self.CombGrndrBrSixthBttlnModPushButton.clicked.connect(self.comb_grndr_the_sixth_bttln_mod_button_was_clicked)
        self.CombGrndrBrSeventhBttlnModPushButton.clicked.connect(self.comb_grndr_the_seventh_bttln_mod_button_was_clicked)

    # заполняем список имен командиров корпуса
    def division_cmndrs_list(self):
        cmndrs_list = self.presenter.DivisionCmndrsNamesList()
        for cmndrName in cmndrs_list:
            self.generalName.addItem(cmndrName)

    def divisionCommanderCostView(self, index):
        value = self.presenter.DivisionCmndrsCost(index)
        self.generalCost.setText(str(value))
        self.divisionTotalCostView()

    def divisionTotalCostView(self):
        total_cost = int(self.generalCost.text()) + int(self.aBrgdTotalCost.text()) +\
                     int(self.bBrgdTotalCost.text()) + int(self.cBrgdTotalCost.text()) +\
                     int(self.JgrBrgdTotalCost.text()) + int(self.CombGrndrBrgdTotalCost.text())

        self.divisionTotalCost.setText(str(total_cost))

    # ------------------------------------------------------------------------------------------------------------------
    def brgdCommanderCostView(self, index, brigade_number, brgdCmndrCost):
        value = self.presenter.BrigadeCmndrsCost(index, brigade_number)
        brgdCmndrCost.setText(str(value))

    def brgdBttlnCostView(self, bttln_choosen_from_list, brigade_number, brgdBattalionCost,
                          brgdTotalCostView, order_number, bttlnModPushButton):
        # отправляем индекс в презентер для передачи в модель чтобы поместить соотетствующий батальон на его место в бригаде
        # order_number =  порядковое место в бригаде
        # индекс выбранного баталльона из списка
        self.presenter.BrigadeBttlnChoosen(order_number, bttln_choosen_from_list, brigade_number)
        # отправляем запрос стоимости батальона стоящего на соответствующем месте в бригаде
        value = self.presenter.BrigadeBttlnCost(order_number, brigade_number)
        # записываем в соответствующее поле значение стоимости батальона
        brgdBattalionCost.setText(str(value))
        brgdTotalCostView()
        if bttlnModPushButton != None:
            self.check_bttln_bonus_for_button_color(order_number, brigade_number, bttlnModPushButton)


    # -------------------------------------------------------------------------------------------------------------------
    def a_brigade_bttln_Lists(self):
        inf_brigade_bttln_Lists(self.a_brigade_number, self.presenter, self.aBrgdCmndr, self.aBrgdFirstBattalion,
                                self.aBrgdSecondBattalion, self.aBrgdThirdBattalion, self.aBrgdFourthBattalion,
                                self.aBrgdAdditionalBattalion)

    def aBrgdCommanderCostView(self, index):
        self.brgdCommanderCostView(index, self.a_brigade_number, self.aBrgdCmndrCost)
        self.aBrgdTotalCostView()
        if self.aBrgdCmndr.currentIndex() < 1:
            self.aBrgdFirstBattalion.setCurrentIndex(0)
            self.aBrgdFirstBattalion.setDisabled(True)
            self.aBrgdSecondBattalion.setCurrentIndex(0)
            self.aBrgdSecondBattalion.setDisabled(True)
            self.aBrgdThirdBattalion.setCurrentIndex(0)
            self.aBrgdThirdBattalion.setDisabled(True)
            self.aBrgdFourthBattalion.setCurrentIndex(0)
            self.aBrgdFourthBattalion.setDisabled(True)
            self.aBrgdAdditionalBattalion.setCurrentIndex(0)
            self.aBrgdAdditionalBattalion.setDisabled(True)

            self.aBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBrAddBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            # self.aBrgdFirstBattalion.setDisabled(False)
            self.aBrgdFirstBattalion.setCurrentIndex(1)
            self.aBrgdSecondBattalion.setDisabled(False)
            self.aBrgdThirdBattalion.setDisabled(False)
            self.aBrgdFourthBattalion.setDisabled(False)
            self.aBrgdAdditionalBattalion.setDisabled(False)

            self.check_bttln_bonus_for_button_color(0, self.a_brigade_number, self.aBrFirstBttlnModPushButton)
            # self.check_bttln_bonus_for_button_color(1, self.a_brigade_number, self.aBrSecondBttlnModPushButton)
            # self.check_bttln_bonus_for_button_color(2, self.a_brigade_number, self.aBrThirdBttlnModPushButton)
            # self.check_bttln_bonus_for_button_color(3, self.a_brigade_number, self.aBrFourthBttlnModPushButton)
            # self.check_bttln_bonus_for_button_color(4, self.a_brigade_number, self.aBrAddBttlnModPushButton)


    def aBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdFirstBattalionCost, self.aBrgdTotalCostView, 0, self.aBrFirstBttlnModPushButton)

    def aBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdSecondBattalionCost, self.aBrgdTotalCostView, 1, self.aBrSecondBttlnModPushButton)

    def aBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdThirdBattalionCost, self.aBrgdTotalCostView, 2, self.aBrFourthBttlnModPushButton)

    def aBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdFourthBattalionCost, self.aBrgdTotalCostView, 3, self.aBrThirdBttlnModPushButton)

    def aBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdAddBattalionCost, self.aBrgdTotalCostView, 4, self.aBrAddBttlnModPushButton)

    def aBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.aBrgdCmndr.currentIndex(), self.a_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.a_brigade_number) for i in range(5))

        self.aBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()

    def a_the_first_bttln_mod_button_was_clicked(self):
        if self.aBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.aBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFirstBattalionCostSetText = self.aBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrFirstBttlnModPushButton)

    def a_the_second_bttln_mod_button_was_clicked(self):
        if self.aBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.aBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSecondBattalionCostSetText = self.aBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrSecondBttlnModPushButton)

    def a_the_third_bttln_mod_button_was_clicked(self):
        if self.aBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.aBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdThirdBattalionCostSetText = self.aBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrThirdBttlnModPushButton)

    def a_the_fourth_bttln_mod_button_was_clicked(self):
        if self.aBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.aBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFourthBattalionCostSetText = self.aBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrFourthBttlnModPushButton)

    def a_the_add_bttln_mod_button_was_clicked(self):
        if self.aBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.aBrgdAdditionalBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.aBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrAddBttlnModPushButton)

    # -------------------------------------------------------------------------------------------------------------------
    def b_brigade_bttln_Lists(self):
        inf_brigade_bttln_Lists(self.b_brigade_number, self.presenter, self.bBrgdCmndr, self.bBrgdFirstBattalion,
                                self.bBrgdSecondBattalion, self.bBrgdThirdBattalion, self.bBrgdFourthBattalion,
                                self.bBrgdAdditionalBattalion)

    # описание кнопок второй бригады
    def bBrgdCommanderCostView(self, index):
        self.brgdCommanderCostView(index, self.b_brigade_number, self.bBrgdCmndrCost)
        self.bBrgdTotalCostView()

        if self.bBrgdCmndr.currentIndex() < 1:
            self.bBrgdFirstBattalion.setCurrentIndex(0)
            self.bBrgdFirstBattalion.setDisabled(True)
            self.bBrgdSecondBattalion.setCurrentIndex(0)
            self.bBrgdSecondBattalion.setDisabled(True)
            self.bBrgdThirdBattalion.setCurrentIndex(0)
            self.bBrgdThirdBattalion.setDisabled(True)
            self.bBrgdFourthBattalion.setCurrentIndex(0)
            self.bBrgdFourthBattalion.setDisabled(True)
            self.bBrgdAdditionalBattalion.setCurrentIndex(0)
            self.bBrgdAdditionalBattalion.setDisabled(True)

            self.bBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.bBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.bBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.bBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.bBrAddBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
        else:
            self.bBrgdFirstBattalion.setCurrentIndex(1)
            self.bBrgdSecondBattalion.setDisabled(False)
            self.bBrgdThirdBattalion.setDisabled(False)
            self.bBrgdFourthBattalion.setDisabled(False)
            self.bBrgdAdditionalBattalion.setDisabled(False)

            self.check_bttln_bonus_for_button_color(0, self.b_brigade_number, self.bBrFirstBttlnModPushButton)

    def bBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdFirstBattalionCost, self.bBrgdTotalCostView, 0, self.bBrFirstBttlnModPushButton)

    def bBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdSecondBattalionCost, self.bBrgdTotalCostView, 1, self.bBrSecondBttlnModPushButton)

    def bBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdThirdBattalionCost, self.bBrgdTotalCostView, 2, self.bBrThirdBttlnModPushButton)

    def bBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdFourthBattalionCost, self.bBrgdTotalCostView, 3, self.bBrFourthBttlnModPushButton)

    def bBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdAddBattalionCost, self.bBrgdTotalCostView, 4, self.bBrAddBttlnModPushButton)

    def bBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.bBrgdCmndr.currentIndex(), self.b_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.b_brigade_number) for i in range(5))

        self.bBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()

    def b_the_first_bttln_mod_button_was_clicked(self):

        if self.bBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.bBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFirstBattalionCostSetText = self.bBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrFirstBttlnModPushButton)

    def b_the_second_bttln_mod_button_was_clicked(self):

        if self.bBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.bBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSecondBattalionCostSetText = self.bBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrSecondBttlnModPushButton)

    def b_the_third_bttln_mod_button_was_clicked(self):

        if self.bBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.bBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdThirdBattalionCostSetText = self.bBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrThirdBttlnModPushButton)

    def b_the_fourth_bttln_mod_button_was_clicked(self):

        if self.bBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.bBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFourthBattalionCostSetText = self.bBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrFourthBttlnModPushButton)

    def b_the_add_bttln_mod_button_was_clicked(self):

        if self.bBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.bBrgdAdditionalBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.bBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrAddBttlnModPushButton)

    # -------------------------------------------------------------------------------------------------------------------

    def c_brigade_bttln_Lists(self):
        inf_brigade_bttln_Lists(self.c_brigade_number, self.presenter, self.cBrgdCmndr, self.cBrgdFirstBattalion,
                                self.cBrgdSecondBattalion, self.cBrgdThirdBattalion, self.cBrgdFourthBattalion,
                                self.cBrgdAdditionalBattalion)

    def cBrgdCommanderCostView(self, index):
        self.brgdCommanderCostView(index, self.c_brigade_number, self.cBrgdCmndrCost)
        self.cBrgdTotalCostView()

        if self.cBrgdCmndr.currentIndex() < 1:
            self.cBrgdFirstBattalion.setCurrentIndex(0)
            self.cBrgdFirstBattalion.setDisabled(True)
            self.cBrgdSecondBattalion.setCurrentIndex(0)
            self.cBrgdSecondBattalion.setDisabled(True)
            self.cBrgdThirdBattalion.setCurrentIndex(0)
            self.cBrgdThirdBattalion.setDisabled(True)
            self.cBrgdFourthBattalion.setCurrentIndex(0)
            self.cBrgdFourthBattalion.setDisabled(True)
            self.cBrgdAdditionalBattalion.setCurrentIndex(0)
            self.cBrgdAdditionalBattalion.setDisabled(True)

            self.cBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.cBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.cBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.cBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.cBrAddBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
        else:
            self.cBrgdFirstBattalion.setCurrentIndex(1)
            self.cBrgdSecondBattalion.setDisabled(False)
            self.cBrgdThirdBattalion.setDisabled(False)
            self.cBrgdFourthBattalion.setDisabled(False)
            self.cBrgdAdditionalBattalion.setDisabled(False)

            self.check_bttln_bonus_for_button_color(0, self.c_brigade_number, self.cBrFirstBttlnModPushButton)


    def cBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdFirstBattalionCost, self.cBrgdTotalCostView, 0, self.cBrFirstBttlnModPushButton)

    def cBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdSecondBattalionCost, self.cBrgdTotalCostView, 1, self.cBrSecondBttlnModPushButton)

    def cBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdThirdBattalionCost, self.cBrgdTotalCostView, 2, self.cBrThirdBttlnModPushButton)

    def cBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdFourthBattalionCost, self.cBrgdTotalCostView, 3, self.cBrFourthBttlnModPushButton)

    def cBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdAddBattalionCost, self.cBrgdTotalCostView, 4, self.cBrAddBttlnModPushButton)

    def cBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.cBrgdCmndr.currentIndex(), self.c_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.c_brigade_number) for i in range(5))

        self.cBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()

    def c_the_first_bttln_mod_button_was_clicked(self):

        if self.cBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.cBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFirstBattalionCostSetText = self.cBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrFirstBttlnModPushButton)

    def c_the_second_bttln_mod_button_was_clicked(self):

        if self.cBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.cBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSecondBattalionCostSetText = self.cBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrSecondBttlnModPushButton)

    def c_the_third_bttln_mod_button_was_clicked(self):

        if self.cBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.cBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdThirdBattalionCostSetText = self.cBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrThirdBttlnModPushButton)

    def c_the_fourth_bttln_mod_button_was_clicked(self):

        if self.cBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.cBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFourthBattalionCostSetText = self.cBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrFourthBttlnModPushButton)

    def c_the_add_bttln_mod_button_was_clicked(self):

        if self.cBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.cBrgdAdditionalBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.cBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrAddBttlnModPushButton)

    # -------------------------------------------------------------------------------------------------------------------
    def jgr_brigade_bttln_Lists(self):
        jgr_brigade_bttln_Lists(self.jgr_brigade_number, self.presenter, self.JgrBrgdCmndr, self.JgrBrgdFirstBattalion,
                                self.JgrBrgdSecondBattalion, self.JgrBrgdThirdBattalion, self.JgrBrgdFourthBattalion,
                                self.JgrBrgdFifthBattalion, self.JgrBrgdSixthBattalion,
                                self.JgrBrgdAdditional1Battalion,
                                self.JgrBrgdAdditional2Battalion)

    def jgrBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.jgr_brigade_number)
        self.JgrBrgdCmndrCost.setText(str(value))
        self.jgrBrgdTotalCostView()

        if self.JgrBrgdCmndr.currentIndex() < 1:
            self.JgrBrgdFirstBattalion.setCurrentIndex(0)
            self.JgrBrgdFirstBattalion.setDisabled(True)
            self.JgrBrgdSecondBattalion.setCurrentIndex(0)
            self.JgrBrgdSecondBattalion.setDisabled(True)
            self.JgrBrgdThirdBattalion.setCurrentIndex(0)
            self.JgrBrgdThirdBattalion.setDisabled(True)
            self.JgrBrgdFourthBattalion.setCurrentIndex(0)
            self.JgrBrgdFourthBattalion.setDisabled(True)
            self.JgrBrgdFifthBattalion.setCurrentIndex(0)
            self.JgrBrgdFifthBattalion.setDisabled(True)
            self.JgrBrgdSixthBattalion.setCurrentIndex(0)
            self.JgrBrgdSixthBattalion.setDisabled(True)
            self.JgrBrgdAdditional1Battalion.setCurrentIndex(0)
            self.JgrBrgdAdditional1Battalion.setDisabled(True)
            self.JgrBrgdAdditional2Battalion.setCurrentIndex(0)
            self.JgrBrgdAdditional2Battalion.setDisabled(True)

            self.JgrBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrFifthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrSixthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
        else:
            self.JgrBrgdFirstBattalion.setCurrentIndex(1)
            self.JgrBrgdSecondBattalion.setCurrentIndex(1)
            self.JgrBrgdThirdBattalion.setDisabled(False)
            self.JgrBrgdFourthBattalion.setDisabled(False)
            self.JgrBrgdFifthBattalion.setDisabled(False)
            self.JgrBrgdSixthBattalion.setDisabled(False)
            self.JgrBrgdAdditional1Battalion.setDisabled(False)
            self.JgrBrgdAdditional2Battalion.setDisabled(False)

    def jgrBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdFirstBattalionCost, self.jgrBrgdTotalCostView, 0, self.JgrBrFirstBttlnModPushButton)

    def jgrBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdSecondBattalionCost, self.jgrBrgdTotalCostView, 1, self.JgrBrSecondBttlnModPushButton)

    def jgrBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdThirdBattalionCost, self.jgrBrgdTotalCostView, 2, self.JgrBrThirdBttlnModPushButton)

    def jgrBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdFourthBattalionCost, self.jgrBrgdTotalCostView, 3, self.JgrBrFourthBttlnModPushButton)

    def jgrBrgd5thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdFifthBattalionCost, self.jgrBrgdTotalCostView, 4, self.JgrBrFifthBttlnModPushButton)

    def jgrBrgd6thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdSixthBattalionCost, self.jgrBrgdTotalCostView, 5, self.JgrBrSixthBttlnModPushButton)

    def jgrBrgdAdd1BttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdAdd1BattalionCost, self.jgrBrgdTotalCostView, 6, None)

    def jgrBrgdAdd2BttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdAdd2BattalionCost, self.jgrBrgdTotalCostView, 7, None)

    def jgrBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.JgrBrgdCmndr.currentIndex(),
                                                      self.jgr_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.jgr_brigade_number) for i in range(8))

        self.JgrBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()

    def jgr_the_first_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.JgrBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFirstBattalionCostSetText = self.JgrBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrFirstBttlnModPushButton)

    def jgr_the_second_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.JgrBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSecondBattalionCostSetText = self.JgrBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrSecondBttlnModPushButton)

    def jgr_the_third_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.JgrBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdThirdBattalionCostSetText = self.JgrBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrThirdBttlnModPushButton)

    def jgr_the_fourth_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.JgrBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFourthBattalionCostSetText = self.JgrBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrFourthBttlnModPushButton)

    def jgr_the_fifth_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdFifthBattalion.currentIndex() != 0:
            battalion_order = "Fifth Battalion"
            self.order_number = 4  # четвертый по порядку батальон
            self.current_bttln_index = self.JgrBrgdFifthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.JgrBrgdFifthBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrFifthBttlnModPushButton)

    def jgr_the_sixth_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdSixthBattalion.currentIndex() != 0:
            battalion_order = "Sixth Battalion"
            self.order_number = 5  # четвертый по порядку батальон
            self.current_bttln_index = self.JgrBrgdSixthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSixthBattalionCostSetText = self.JgrBrgdSixthBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrSixthBttlnModPushButton)

    # -------------------------------------------------------------------------------------------------------------------
    def comb_grndr_brigade_bttln_Lists(self):
        comb_grndr_brigade_bttln_Lists(self.comb_grndr_brigade_number, self.presenter, self.CombGrndrBrgdCmndr, self.CombGrndrBrgdFirstBattalion,
                                self.CombGrndrBrgdSecondBattalion, self.CombGrndrBrgdThirdBattalion, self.CombGrndrBrgdFourthBattalion,
                                self.CombGrndrBrgdFifthBattalion, self.CombGrndrBrgdSixthBattalion, self.CombGrndrBrgdSeventhBattalion
                                )
    def combGrndrBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.comb_grndr_brigade_number)
        self.CombGrndrBrgdCmndrCost.setText(str(value))
        self.combGrndrBrgdTotalCostView()

        if self.CombGrndrBrgdCmndr.currentIndex() < 1:
            self.CombGrndrBrgdFirstBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdFirstBattalion.setDisabled(True)
            self.CombGrndrBrgdSecondBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdSecondBattalion.setDisabled(True)
            self.CombGrndrBrgdThirdBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdThirdBattalion.setDisabled(True)
            self.CombGrndrBrgdFourthBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdFourthBattalion.setDisabled(True)
            self.CombGrndrBrgdFifthBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdFifthBattalion.setDisabled(True)
            self.CombGrndrBrgdSixthBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdSixthBattalion.setDisabled(True)
            self.CombGrndrBrgdSeventhBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdSeventhBattalion.setDisabled(True)

            self.CombGrndrBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrFifthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrSixthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrSeventhBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
        else:
            self.CombGrndrBrgdFirstBattalion.setCurrentIndex(1)
            self.CombGrndrBrgdSecondBattalion.setCurrentIndex(1)
            self.CombGrndrBrgdThirdBattalion.setDisabled(False)
            self.CombGrndrBrgdFourthBattalion.setDisabled(False)
            self.CombGrndrBrgdFifthBattalion.setDisabled(False)
            self.CombGrndrBrgdSixthBattalion.setDisabled(False)
            self.CombGrndrBrgdSeventhBattalion.setDisabled(False)

    def combGrndrBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdFirstBattalionCost, self.combGrndrBrgdTotalCostView, 0, self.CombGrndrBrFirstBttlnModPushButton)

    def combGrndrBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdSecondBattalionCost, self.combGrndrBrgdTotalCostView, 1, self.CombGrndrBrSecondBttlnModPushButton)

    def combGrndrBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdThirdBattalionCost, self.combGrndrBrgdTotalCostView, 2, self.CombGrndrBrThirdBttlnModPushButton)

    def combGrndrBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdFourthBattalionCost, self.combGrndrBrgdTotalCostView, 3, self.CombGrndrBrFourthBttlnModPushButton)

    def combGrndrBrgd5thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdFifthBattalionCost, self.combGrndrBrgdTotalCostView, 4, self.CombGrndrBrFifthBttlnModPushButton)

    def combGrndrBrgd6thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdSixthBattalionCost, self.combGrndrBrgdTotalCostView, 5, self.CombGrndrBrSixthBttlnModPushButton)

    def combGrndrBrgd7thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdSeventhBattalionCost, self.combGrndrBrgdTotalCostView, 6, self.CombGrndrBrSeventhBttlnModPushButton)

    def combGrndrBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.CombGrndrBrgdCmndr.currentIndex(),self.comb_grndr_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.comb_grndr_brigade_number) for i in range(7))

        self.CombGrndrBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()


    def comb_grndr_the_first_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.current_bttln_index = self.CombGrndrBrgdFirstBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFirstBattalionCostSetText = self.CombGrndrBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrFirstBttlnModPushButton)

    def comb_grndr_the_second_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.CombGrndrBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSecondBattalionCostSetText = self.CombGrndrBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrSecondBttlnModPushButton)

    def comb_grndr_the_third_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.CombGrndrBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdThirdBattalionCostSetText = self.CombGrndrBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrThirdBttlnModPushButton)

    def comb_grndr_the_fourth_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.CombGrndrBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFourthBattalionCostSetText = self.CombGrndrBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrFourthBttlnModPushButton)

    def comb_grndr_the_fifth_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdFifthBattalion.currentIndex() != 0:
            battalion_order = "Fifth Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.current_bttln_index = self.CombGrndrBrgdFifthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdFifthBattalionCostSetText = self.CombGrndrBrgdFifthBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrFifthBttlnModPushButton)

    def comb_grndr_the_sixth_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdSixthBattalion.currentIndex() != 0:
            battalion_order = "Sixth Battalion"
            self.order_number = 5  # шестой по порядку батальон
            self.current_bttln_index = self.CombGrndrBrgdSixthBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSixthBattalionCostSetText = self.CombGrndrBrgdSixthBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrSixthBttlnModPushButton)

    def comb_grndr_the_seventh_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdSeventhBattalion.currentIndex() != 0:
            battalion_order = "Seventh Battalion"
            self.order_number = 6  # седьмой по порядку батальон
            self.current_bttln_index = self.CombGrndrBrgdSeventhBattalion.currentIndex()  # имя батальона выбраного на данный момент
            self.brgdSeventhBattalionCostSetText = self.CombGrndrBrgdSeventhBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrSeventhBttlnModPushButton)


    #--------------------------------------------------------------------------------------------------------------------

    def bttln_mod_button_was_clicked(self, battalion_order, brigade_number, mod_button_name):

        self.brigade_number = brigade_number
        self.bonus_window = BonusWindow()
        self.bonus_window.setWindowTitle(battalion_order)
        self.mod_button_name = mod_button_name

        self.bonuses = [
            "",
            "",
            "",
            "",
            "",
            ""
        ]

        self.bonuses_list_in_window = [
            self.bonus_window.bonus1,
            self.bonus_window.bonus2,
            self.bonus_window.bonus3,
            self.bonus_window.bonus4,
            self.bonus_window.bonus5,
            self.bonus_window.bonus6
        ]

        self.bonuses_checkboxes_in_window = [
            self.bonus_window.checkBox_1,
            self.bonus_window.checkBox_2,
            self.bonus_window.checkBox_3,
            self.bonus_window.checkBox_4,
            self.bonus_window.checkBox_5,
            self.bonus_window.checkBox_6
        ]

        checkbox_Action_list =[
            self.checkBox1_Action,
            self.checkBox2_Action,
            self.checkBox3_Action
        ]

        # создаем временную переменную стоимости батальона , для отображения в окне бонусов
        self.temporary_bonus_cost = self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)
        # создаем временный список бонусов батальона
        self.temporary_bonus_list = self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number).copy()

        self.bonus_window.name.setText(str(self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number)))
        self.bonus_window.cost.setText(str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))

        self.btln_bonus_list =[]
        self.btln_bonus_cost_list = []

        apply_bonus_count = 0
        for bonus_count in range (0, len(self.presenter.BrigadeBonusNameList(self.brigade_number))):
            # проверяем Имя текущего батальона находится среди имен батальонов списка соответствия бонуса к батальонам
            if self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number) in self.presenter.BrigadeBonusToBattalion(self.presenter.BrigadeBonusNameList(self.brigade_number)[bonus_count], self.brigade_number):

                self.bonuses_list_in_window[apply_bonus_count].setText(self.presenter.BrigadeBonusNameList(self.brigade_number)[bonus_count])
                #создаем локальтный список всех возможных бонусов батальона
                self.btln_bonus_list.append(self.presenter.BrigadeBonusNameList(self.brigade_number)[bonus_count])
                self.btln_bonus_cost_list.append(self.presenter.BrigadeBonusCostList(self.brigade_number)[bonus_count])

                apply_bonus_count +=1

        #закрываем оставшиеся ненужные строки
        for i in range (apply_bonus_count, len(self.bonuses_list_in_window)):
            self.bonuses_list_in_window[i].close()
            self.bonuses_checkboxes_in_window[i].close()

        # расставляем статус "нажато" если такой бонус был ранее добавлен
        for i in range (0, len(self.btln_bonus_list)):
            if self.btln_bonus_list[i] in self.presenter.BrigadeBttlnBonusList(
                    self.order_number, self.brigade_number):
                self.bonuses_checkboxes_in_window[i].setChecked(True)
            self.bonuses_checkboxes_in_window[i].stateChanged.connect(checkbox_Action_list[i])

        self.bonus_window.ok_button.clicked.connect(self.ok_button_was_clicked)
        self.bonus_window.cancel_button.clicked.connect(self.cancel_button_was_clicked)
        self.bonus_window.show()

    def ok_button_was_clicked(self):

        # проверка - не переключил ли пользователь отряд , пока открыто окно выбора бонусов
        if self.current_bttln_index != 0:

            for i in range(0, len(self.btln_bonus_list)):
                # проверка если выбранный бонус не пуст то тогда применяются свойства бонууса.
                if self.bonuses[i] != "":
                    # проверяем если чекбокс был нажат то добавляем свойста, если отжат , то удаляем свойства и стоимость
                    if self.bonuses_checkboxes_in_window[i].isChecked():
                        # проверяем, если такой такого юонуса еще нет то добавляем
                        if self.btln_bonus_list[i] not in self.presenter.BrigadeBttlnBonusList(self.order_number,self.brigade_number):
                            self.presenter.BrigadeBttlnBonusAdd(self.bonuses[i], self.order_number, self.brigade_number)
                            self.presenter.BrigadeBttlnBonusCostAdd(self.btln_bonus_cost_list[i], self.order_number,self.brigade_number)
                    else:
                        # проверяем, если такой бонус есть то удаляем
                        if self.btln_bonus_list[i] in self.presenter.BrigadeBttlnBonusList(self.order_number,self.brigade_number):
                            self.presenter.BrigadeBttlnBonusDel(self.bonuses[i], self.order_number, self.brigade_number)
                            self.presenter.BrigadeBttlnBonusCostAdd(self.btln_bonus_cost_list[i] * (-1),self.order_number, self.brigade_number)

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
                case 6:
                    self.brgdSeventhBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))



            # и обновляем полную стоимость бригады
            self.brgdTotalCostView()
            # перекрашиваем кнупку если надо
            self.check_bttln_bonus_for_button_color(self.order_number, self.brigade_number, self.mod_button_name)
            self.bonus_window.close()
        else:
            self.cancel_button_was_clicked()

    def cancel_button_was_clicked(self):
        self.bonus_window.close()

    def check_bttln_bonus_for_button_color(self, order_number, brigade_number, mod_button_name):
        if len(self.presenter.BrigadeBttlnBonusList(order_number, brigade_number)) == 0:
            mod_button_name.setStyleSheet("background-color : rgb(225,225,225) ")
        else:
            mod_button_name.setStyleSheet("background-color : white")

    def checkBox1_Action(self):
        self.checkBox_Action(0)

    def checkBox2_Action(self):
        self.checkBox_Action(1)

    def checkBox3_Action(self):
        self.checkBox_Action(2)

    def checkBox_Action(self, order_number):
        self.bonuses[order_number] = self.btln_bonus_list[order_number]

        # проверка если чекбокс нажат и такого бонуса еще нет в списке бонусов батальона, то в окне отображения бонусов показывается стоимость с бонусом ()
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс нажат и такой бонус уже есть, то показывается стоимость взятая из обьекта батальон
        if self.bonuses_checkboxes_in_window[order_number].isChecked():
            if self.btln_bonus_list[order_number] not in self.temporary_bonus_list:
                self.temporary_bonus_cost += self.btln_bonus_cost_list[order_number]  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list[self.btln_bonus_list[order_number]] = None  # вносим бонус во временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
        # проверка если чекбокс отжат и такой бонус есть в списке бонусов батальона, то в окне отображения бонусов показывается стоимость за вычетом бонуса
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс отжат  и такого бонуса нет, то показывается стоимость взятая из обьекта батальон
        else:
            if self.btln_bonus_list[order_number] in self.temporary_bonus_list:
                self.temporary_bonus_cost -= self.btln_bonus_cost_list[order_number]  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list[self.btln_bonus_list[order_number] ]  # удаляем бонус из временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))