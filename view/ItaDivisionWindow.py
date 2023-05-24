import json

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from fpdf import FPDF, XPos, YPos, Align

from presenter.presenter import Presenter
from view.ItaDivisionGuiWindow import Ui_ItaDivisionWindow
from view.BonusWindow import BonusWindow
from view.E_message import MessageWindow

from view.brigades.brigade_view import brigade_bttln_Lists

class ItaDivisionWindow(QtWidgets.QMainWindow, Ui_ItaDivisionWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(ItaDivisionWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.error_message = MessageWindow()

        # self.actionSave.triggered.connect(self.saveFile)
        # self.actionExport_army_list_to_PDF.triggered.connect(self.exportToPDF)

        self.country = "Ita"  # определяем страну
        self.presenter = Presenter(self.country)
        self.generalName.currentIndexChanged.connect(self.divisionCommanderCostView)

         # изменяемая переменная для прхождения проверки  - используется для кавполков с неоднозначным выбором первоко полка в списке, при изменении списка
        self.a_brigade_number = 0  # номер бригады попорядку
        self.a_battalion_index_add = 0
        self.a1_choice_add = 0
        self.a1_shift_battallion_order = 0
        self.a_first_regiment_choice_run_flag = True # флаг отсекающий вызов действия по изменению параметра списка при очистве списка
        self.a2_battalion_index_add = 0
        self.a2_choice_add = 0
        self.a2_shift_battallion_order = 0

# первый полк
        self.aBrgdCmndr.currentIndexChanged.connect(self.aBrgdCommanderCostView)
        self.aBrgd1stRgmntChoice.currentIndexChanged.connect(self.aBrgd1stRgmntChoiceView)
        self.aBrgd1stRgmntFirstBattalion.currentIndexChanged.connect(self.aBrgd1stRgmnt1stBttlnCostView)
        self.aBrgd1stRgmntSecondBattalion.currentIndexChanged.connect(self.aBrgd1stRgmnt2ndBttlnCostView)
        self.aBrgd1stRgmntThirdBattalion.currentIndexChanged.connect(self.aBrgd1stRgmnt3rdBttlnCostView)
        self.aBrgd1stRgmntFourthBattalion.currentIndexChanged.connect(self.aBrgd1stRgmnt4thBttlnCostView)

        self.aBr1stRgmntFirstBttlnModPushButton.clicked.connect(self.a_the_first_bttln_mod_button_was_clicked)
        self.aBr1stRgmntSecondBttlnModPushButton.clicked.connect(self.a_the_second_bttln_mod_button_was_clicked)
        self.aBr1stRgmntThirdBttlnModPushButton.clicked.connect(self.a_the_third_bttln_mod_button_was_clicked)
        self.aBr1stRgmntFourthBttlnModPushButton.clicked.connect(self.a_the_fourth_bttln_mod_button_was_clicked)
# воройй полк
        self.aBrgd2ndRgmntChoice.currentIndexChanged.connect(self.aBrgd2ndRgmntChoiceView)
        self.aBrgd2ndRgmntFirstBattalion.currentIndexChanged.connect(self.aBrgd2ndRgmnt1stBttlnCostView)
        self.aBrgd2ndRgmntSecondBattalion.currentIndexChanged.connect(self.aBrgd2ndRgmnt2ndBttlnCostView)
        self.aBrgd2ndRgmntThirdBattalion.currentIndexChanged.connect(self.aBrgd2ndRgmnt3rdBttlnCostView)
        self.aBrgd2ndRgmntFourthBattalion.currentIndexChanged.connect(self.aBrgd2ndRgmnt4thBttlnCostView)

        self.aBr2ndRgmntFirstBttlnModPushButton.clicked.connect(self.a_the_fifth_bttln_mod_button_was_clicked)
        self.aBr2ndRgmntSecondBttlnModPushButton.clicked.connect(self.a_the_sixth_bttln_mod_button_was_clicked)
        self.aBr2ndRgmntThirdBttlnModPushButton.clicked.connect(self.a_the_seventh_bttln_mod_button_was_clicked)
        self.aBr2ndRgmntFourthBttlnModPushButton.clicked.connect(self.a_the_eighth_bttln_mod_button_was_clicked)

# дополнительные артроты

        self.aBrgd1stRgmntAddBttry.currentIndexChanged.connect(self.aBrgd1stRgmntAddBttryCostView)
        self.aBrgd2ndRgmntAddBttry.currentIndexChanged.connect(self.aBrgd2ndRgmntAddBttryCostView)

#
    # заполняем список имен командиров дивизии
    def division_cmndrs_list(self):
        cmndrs_list = self.presenter.DivisionCmndrsNamesList()
        for cmndrName in cmndrs_list:
            self.generalName.addItem(cmndrName)

    def divisionCommanderCostView(self, index):
        value = self.presenter.DivisionCmndrCost(index)
        self.generalCost.setText(str(value))
        self.divisionTotalCostView()

    def divisionTotalCostView(self):

          total_cost = int(self.generalCost.text())
          self.divisionTotalCost.setText(str(total_cost))


#     # ------------------------------------------------------------------------------------------------------------------
   #запрос через дивизию стоимости текущего командира бригалы и установка его значения в окно
    def brgdCommanderCostView(self, index, brigade_number, brgdCmndrCost):
        value = self.presenter.BrigadeCmndrsCost(index, brigade_number)
        brgdCmndrCost.setText(str(value))

    def brgdBttlnCostView(self, bttln_choosen_from_list, brigade_number, brgdBattalionCost, brgdTotalCostView, order_number, bttlnModPushButton, shift):
        # отправляем индекс в презентер для передачи в модель чтобы поместить соотетствующий батальон на его место в бригаде
        # order_number =  порядковое место в бригаде
        # индекс выбранного баталльона из списка
        self.presenter.BrigadeBttlnChoosen(order_number, bttln_choosen_from_list, brigade_number, shift)
        # отправляем запрос стоимости батальона стоящего на соответствующем месте в бригаде

        if bttlnModPushButton != None:
            self.check_bttln_bonus_for_button_color(order_number, brigade_number, bttlnModPushButton)

        value = self.presenter.BrigadeBttlnCost(order_number, brigade_number)
        # записываем в соответствующее поле значение стоимости батальона
        brgdBattalionCost.setText(str(value))
        brgdTotalCostView()

#
#
#     # -------------------------------------------------------------------------------------------------------------------
    def a_brigade_1stReg_choice(self):
        self.brigade_Reg_choice(self.aBrgd1stRgmntChoice)
    def a_brigade_1stReg_choice_short(self):
        self.brigade_Reg_choice_short(self.aBrgd1stRgmntChoice)

    def a_brigade_2ndReg_choice(self):
        self.brigade_Reg_choice(self.aBrgd2ndRgmntChoice)


    def brigade_Reg_choice(self, regimentChoice):
        regimentChoice.addItem("empty")
        regimentChoice.addItem("Line Infantry")
        regimentChoice.addItem("Light Infantry")

    def brigade_Reg_choice_short(self, regimentChoice):
        regimentChoice.addItem("Line Infantry")
        regimentChoice.addItem("Light Infantry")

    def aBrgdCommanderCostView(self, index):
         self.brgdCommanderCostView(index, self.a_brigade_number, self.aBrgdCmndrCost)  # записали стоимость командира в окно
         self.aBrgdTotalCostView()                                                      # посчитали стоимость бригады
         if self.aBrgdCmndr.currentIndex() < 1:                     # если утанавливается первое значение в выборе командира (а там должно стоять empty)
              self.a1_choice_add = 0                                # флаг первого значения вписке 0  - emppty в полном списке
              if self.aBrgd1stRgmntChoice.currentText() != "empty": # если в выборе полка стоит не пусто
                  self.a_first_regiment_choice_run_flag = False
                  self.aBrgd1stRgmntChoice.clear()                  # стереть текущий список выбора полка
                  self.a_first_regiment_choice_run_flag = True
                  self.a_brigade_1stReg_choice()                    # записать полный спиок (с empty впереди)

              self.aBrgd1stRgmntChoice.setCurrentIndex(0)           # выбор полка становится empty
              self.aBrgd1stRgmntChoice.setDisabled(True)            # и возможность выбора бокируется.
              self.aBrgd2ndRgmntChoice.setCurrentIndex(0)           # выбор полка становится empty
              self.aBrgd2ndRgmntChoice.setDisabled(True)
         else:                                                  # если утанавливается любое не empty значение в выборе командира
             if self.a1_choice_add == 0:        # флаг - полного списка и того ,что empty в списке полка стоит на 0 месте
                 self.a1_choice_add = 1         # изменяем флаг на 1 чтобы пройти проверку нулевой позиции списка в дальнейгем
                 self.a_first_regiment_choice_run_flag = False
                 self.aBrgd1stRgmntChoice.clear()                   # очищается полный список выбора полка
                 self.a_first_regiment_choice_run_flag = True
                 self.a_brigade_1stReg_choice_short()               # устанавливается короткий список выбора полка - без empty
                 self.aBrgd1stRgmntChoice.setCurrentIndex(0)
                 self.aBrgd1stRgmntChoice.setDisabled(False)

             self.aBrgd2ndRgmntChoice.setCurrentIndex(0)  # выбор полка становится empty
             self.aBrgd2ndRgmntChoice.setDisabled(False)


    def aBrgd1stRgmntChoiceView(self):
        if self.a_first_regiment_choice_run_flag:

            if self.aBrgd1stRgmntChoice.currentIndex()+self.a1_choice_add < 1:                  # проверка выбранного батальона, если список батальонов не содежит empty

                if self.presenter.BrigadeBttlnName(0, self.a_brigade_number) != "empty":        # есл имя первого батальона бригады оказалось не empty
                    self.presenter.FirstBttlnListChange(0, self.a_brigade_number)               # установим на нулевую позицию первого батальона empty Unit
                    self.presenter.FirstBttlnListChange(10, self.a_brigade_number)
                    self.aBrgd1stRgmntFirstBattalion.clear()                                    # очистим спссок первого батальона
                    bttln_list = self.presenter.BrigadeBttlnList(0, self.a_brigade_number)      # gперезапишем список первого батальона
                    for bttlnName in bttln_list:
                        self.aBrgd1stRgmntFirstBattalion.addItem(bttlnName)

                self.a_battalion_index_add = 0                                              # установим флаг сдвижки первого батальона на 0 - тоесть первый в списке empty

                self.a1_shift_battallion_order = 0                                              # флаг  линейной 0 лии легкой пехты 4 ставим на 0
                self.aBrgd1stRgmntFirstBattalion.setCurrentIndex(0)
                self.aBrgd1stRgmntFirstBattalion.setDisabled(True)                              # все батальоны на 0 - empty и выключаем возможность выбора
                self.aBrgd1stRgmntSecondBattalion.setCurrentIndex(0)
                self.aBrgd1stRgmntSecondBattalion.setDisabled(True)
                self.aBrgd1stRgmntThirdBattalion.setCurrentIndex(0)
                self.aBrgd1stRgmntThirdBattalion.setDisabled(True)
                self.aBrgd1stRgmntFourthBattalion.setCurrentIndex(0)
                self.aBrgd1stRgmntFourthBattalion.setDisabled(True)
                self.aBrgd1stRgmntAddBttry.setCurrentIndex(0)
                self.aBrgd1stRgmntAddBttry.setDisabled(True)

                self.aBr1stRgmntFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
                self.aBr1stRgmntSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
                self.aBr1stRgmntThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
                self.aBr1stRgmntFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

            else:                                                                                                   # если выбор полка - любое другое
                if self.a_battalion_index_add == 0:                                                                     # если при этом флаг сдаидки батальонов = 0 ,  тоесть в списве первым стоит unit  с именем empty
                    # убираем обьект empty из списка выбора
                    self.aBrgd1stRgmntFirstBattalion.clear()                                                            # очищаем список первого батальона
                    self.presenter.FirstBttlnListChangeToShow(0, self.a_brigade_number)                                 # удаляем empty из списка имен батальона
                    self.presenter.FirstBttlnListChangeToShow(10, self.a_brigade_number)
                    bttln_list = self.presenter.BrigadeBttlnList(0, self.a_brigade_number)
                    for bttlnName in bttln_list:                                                                        #  перезаписываем выпадающий список уже без empty
                        self.aBrgd1stRgmntFirstBattalion.addItem(bttlnName)
                    # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                    self.a_battalion_index_add = 1
                    # self.a1_shift_battallion_order = 0

                else:                                                               # если флаг сдвижки батальонов оказался не 0,  тоесть список уже не содержит empty
                    if self.aBrgd1stRgmntChoice.currentIndex() == 0:        # то если выбрана первая позиция - Line Infantry то ставим шаг = 0
                        self.a1_shift_battallion_order = 0

                    else:                                                           # то если выбрана вторая позиция - Liпре Infantry то ставим шаг = 4
                        self.a1_shift_battallion_order = 10


                    self.aBrgd1stRgmntFirstBattalion.clear()                        # очищаем список имен батальонов
                    bttln_list = self.presenter.BrigadeBttlnList(0+self.a1_shift_battallion_order, self.a_brigade_number)
                    for bttlnName in bttln_list:
                        self.aBrgd1stRgmntFirstBattalion.addItem(bttlnName)

                    self.aBrgd1stRgmntSecondBattalion.clear()                        # очищаем список имен батальонов
                    bttln_list = self.presenter.BrigadeBttlnList(1+self.a1_shift_battallion_order, self.a_brigade_number)
                    for bttlnName in bttln_list:
                        self.aBrgd1stRgmntSecondBattalion.addItem(bttlnName)

                    self.aBrgd1stRgmntThirdBattalion.clear()                        # очищаем список имен батальонов
                    bttln_list = self.presenter.BrigadeBttlnList(2+self.a1_shift_battallion_order, self.a_brigade_number)
                    for bttlnName in bttln_list:
                        self.aBrgd1stRgmntThirdBattalion.addItem(bttlnName)

                    self.aBrgd1stRgmntFourthBattalion.clear()                        # очищаем список имен батальонов
                    bttln_list = self.presenter.BrigadeBttlnList(3+self.a1_shift_battallion_order, self.a_brigade_number)
                    for bttlnName in bttln_list:
                        self.aBrgd1stRgmntFourthBattalion.addItem(bttlnName)


                self.aBrgd1stRgmntFirstBattalion.setDisabled(False)
                self.aBrgd1stRgmntSecondBattalion.setDisabled(False)
                self.aBrgd1stRgmntThirdBattalion.setDisabled(False)
                self.aBrgd1stRgmntFourthBattalion.setDisabled(False)
                self.aBrgd1stRgmntAddBttry.setDisabled(False)

    def aBrgd2ndRgmntChoiceView(self):


        if self.aBrgd2ndRgmntChoice.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(4, self.a_brigade_number) != "empty":        # если имя первого батальона бригады оказалось не empty
                self.presenter.FirstBttlnListChange(4, self.a_brigade_number)               # установим на нулевую позицию первого батальона empty Unit
                self.presenter.FirstBttlnListChange(14, self.a_brigade_number)
                self.aBrgd2ndRgmntFirstBattalion.clear()                                    # очистим спссок первого батальона
                bttln_list = self.presenter.BrigadeBttlnList(4, self.a_brigade_number)      # gперезапишем список первого батальона
                for bttlnName in bttln_list:
                    self.aBrgd2ndRgmntFirstBattalion.addItem(bttlnName)
            #
            self.a2_battalion_index_add = 0                                              # установим флаг сдвижки первого батальона на 0 - тоесть первый в списке empty
            #
            self.a2_shift_battallion_order = 0                                              # флаг  линейной 0 лии легкой пехты 8 ставим на 0
            self.aBrgd2ndRgmntFirstBattalion.setCurrentIndex(0)
            self.aBrgd2ndRgmntFirstBattalion.setDisabled(True)                              # все батальоны на 0 - empty и выключаем возможность выбора
            self.aBrgd2ndRgmntSecondBattalion.setCurrentIndex(0)
            self.aBrgd2ndRgmntSecondBattalion.setDisabled(True)
            self.aBrgd2ndRgmntThirdBattalion.setCurrentIndex(0)
            self.aBrgd2ndRgmntThirdBattalion.setDisabled(True)
            self.aBrgd2ndRgmntFourthBattalion.setCurrentIndex(0)
            self.aBrgd2ndRgmntFourthBattalion.setDisabled(True)
            self.aBrgd2ndRgmntAddBttry.setCurrentIndex(0)
            self.aBrgd2ndRgmntAddBttry.setDisabled(True)

            self.aBr2ndRgmntFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBr2ndRgmntSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBr2ndRgmntThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBr2ndRgmntFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:                                                                                                   # если выбор полка - любое другое
            if self.a2_battalion_index_add == 0:                                                                     # если при этом флаг сдаидки батальонов = 0 ,  тоесть в списве первым стоит unit  с именем empty
                # убираем обьект empty из списка выбора
                self.aBrgd2ndRgmntFirstBattalion.clear()                                                            # очищаем список первого батальона
                self.presenter.FirstBttlnListChangeToShow(4, self.a_brigade_number)                                 # удаляем empty из списка имен батальона
                self.presenter.FirstBttlnListChangeToShow(14, self.a_brigade_number)
                self.a2_battalion_index_add = 1

            if self.aBrgd2ndRgmntChoice.currentIndex() == 1:        # то если выбрана первая позиция - Line Infantry то ставим шаг = 0
                self.a2_shift_battallion_order = 0

            if self.aBrgd2ndRgmntChoice.currentIndex() == 2:        # то если выбрана вторая позиция - Liпре Infantry то ставим шаг = 8
                self.a2_shift_battallion_order = 10

            self.aBrgd2ndRgmntFirstBattalion.clear()                        # очищаем список имен батальонов
            bttln_list = self.presenter.BrigadeBttlnList(4+self.a2_shift_battallion_order, self.a_brigade_number)
            for bttlnName in bttln_list:
                self.aBrgd2ndRgmntFirstBattalion.addItem(bttlnName)

            self.aBrgd2ndRgmntSecondBattalion.clear()                        # очищаем список имен батальонов
            bttln_list = self.presenter.BrigadeBttlnList(5+self.a2_shift_battallion_order, self.a_brigade_number)
            for bttlnName in bttln_list:
                self.aBrgd2ndRgmntSecondBattalion.addItem(bttlnName)

            self.aBrgd2ndRgmntThirdBattalion.clear()                        # очищаем список имен батальонов
            bttln_list = self.presenter.BrigadeBttlnList(6+self.a2_shift_battallion_order, self.a_brigade_number)
            for bttlnName in bttln_list:
                self.aBrgd2ndRgmntThirdBattalion.addItem(bttlnName)

            self.aBrgd2ndRgmntFourthBattalion.clear()                        # очищаем список имен батальонов
            bttln_list = self.presenter.BrigadeBttlnList(7+self.a2_shift_battallion_order, self.a_brigade_number)
            for bttlnName in bttln_list:
                self.aBrgd2ndRgmntFourthBattalion.addItem(bttlnName)

            self.aBrgd2ndRgmntFirstBattalion.setDisabled(False)
            self.aBrgd2ndRgmntSecondBattalion.setDisabled(False)
            self.aBrgd2ndRgmntThirdBattalion.setDisabled(False)
            self.aBrgd2ndRgmntFourthBattalion.setDisabled(False)
            self.aBrgd2ndRgmntAddBttry.setDisabled(False)

    def a_brigade_bttln_Lists(self):
        a_brgd_bttlns_list =[self.aBrgd1stRgmntFirstBattalion,
                             self.aBrgd1stRgmntSecondBattalion,
                             self.aBrgd1stRgmntThirdBattalion,
                             self.aBrgd1stRgmntFourthBattalion,
                             self.aBrgd2ndRgmntFirstBattalion,
                             self.aBrgd2ndRgmntSecondBattalion,
                             self.aBrgd2ndRgmntThirdBattalion,
                             self.aBrgd2ndRgmntFourthBattalion,
                             self.aBrgd1stRgmntAddBttry,
                             self.aBrgd2ndRgmntAddBttry,
                             ]

        brigade_bttln_Lists(self.a_brigade_number, self.presenter, self.aBrgdCmndr, a_brgd_bttlns_list)
#





    def aBrgd1stRgmnt1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd1stRgmntFirstBattalionCost, self.aBrgdTotalCostView, 0, self.aBr1stRgmntFirstBttlnModPushButton, self.a1_shift_battallion_order)

    def aBrgd1stRgmnt2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd1stRgmntSecondBattalionCost, self.aBrgdTotalCostView, 1, self.aBr1stRgmntSecondBttlnModPushButton, self.a1_shift_battallion_order)

    def aBrgd1stRgmnt3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd1stRgmntThirdBattalionCost, self.aBrgdTotalCostView, 2, self.aBr1stRgmntThirdBttlnModPushButton, self.a1_shift_battallion_order)

    def aBrgd1stRgmnt4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd1stRgmntFourthBattalionCost, self.aBrgdTotalCostView, 3, self.aBr1stRgmntFourthBttlnModPushButton, self.a1_shift_battallion_order)


    def aBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.aBrgdCmndr.currentIndex(), self.a_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.a_brigade_number) for i in range(10))

        self.a_brgd_1st_rgmt_nmbr_of_battalions = (sum(self.presenter.BrigadeBttlnPresence(i, self.a_brigade_number) for i in range(0, 4)))
        self.a_brgd_2nd_rgmt_nmbr_of_battalions = (sum(self.presenter.BrigadeBttlnPresence(i, self.a_brigade_number) for i in range(4, 8)))

        if self.aBrgd1stRgmntAddBttry.currentText() == "Regimental Artillery Battery":
            if self.a_brgd_1st_rgmt_nmbr_of_battalions < 3:
                self.aBrgd1stRgmntAddBttry.setCurrentIndex(0)

        if self.aBrgd2ndRgmntAddBttry.currentText() == "Regimental Artillery Battery":
            if self.a_brgd_2nd_rgmt_nmbr_of_battalions < 3:
                self.aBrgd2ndRgmntAddBttry.setCurrentIndex(0)

        self.aBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()

    def a_the_first_bttln_mod_button_was_clicked(self):
        if self.aBrgd1stRgmntFirstBattalion.currentIndex()+ self.a_battalion_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.brgdFirstBattalionCostSetText = self.aBrgd1stRgmntFirstBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBr1stRgmntFirstBttlnModPushButton, self.aBrgd1stRgmntFirstBattalion.currentText(), self.order_number)

    def a_the_second_bttln_mod_button_was_clicked(self):
        if self.aBrgd1stRgmntSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.brgdSecondBattalionCostSetText = self.aBrgd1stRgmntSecondBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBr1stRgmntSecondBttlnModPushButton, self.aBrgd1stRgmntSecondBattalion.currentText(), self.order_number)

    def a_the_third_bttln_mod_button_was_clicked(self):
        if self.aBrgd1stRgmntThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2 # третий по порядку батальон
            self.brgdThirdBattalionCostSetText = self.aBrgd1stRgmntThirdBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBr1stRgmntThirdBttlnModPushButton, self.aBrgd1stRgmntThirdBattalion.currentText(), self.order_number)

    def a_the_fourth_bttln_mod_button_was_clicked(self):
        if self.aBrgd1stRgmntFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3# четвертый по порядку батальон
            self.brgdFourthBattalionCostSetText = self.aBrgd1stRgmntFourthBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBr1stRgmntFourthBttlnModPushButton, self.aBrgd1stRgmntFourthBattalion.currentText(), self.order_number)

    def aBrgd2ndRgmnt1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd2ndRgmntFirstBattalionCost, self.aBrgdTotalCostView, 4, self.aBr2ndRgmntFirstBttlnModPushButton, self.a2_shift_battallion_order)

    def aBrgd2ndRgmnt2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd2ndRgmntSecondBattalionCost, self.aBrgdTotalCostView, 5, self.aBr2ndRgmntSecondBttlnModPushButton, self.a2_shift_battallion_order)

    def aBrgd2ndRgmnt3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd2ndRgmntThirdBattalionCost, self.aBrgdTotalCostView, 6, self.aBr2ndRgmntThirdBttlnModPushButton, self.a2_shift_battallion_order)

    def aBrgd2ndRgmnt4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd2ndRgmntFourthBattalionCost, self.aBrgdTotalCostView, 7, self.aBr2ndRgmntFourthBttlnModPushButton, self.a2_shift_battallion_order)

    def a_the_fifth_bttln_mod_button_was_clicked(self):
        if self.aBrgd2ndRgmntFirstBattalion.currentIndex() + self.a2_battalion_index_add != 0:
            battalion_order = "Fifth Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.brgdFifthBattalionCostSetText = self.aBrgd2ndRgmntFirstBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBr2ndRgmntFirstBttlnModPushButton,
                                              self.aBrgd2ndRgmntFirstBattalion.currentText(), self.order_number)

    def a_the_sixth_bttln_mod_button_was_clicked(self):
        if self.aBrgd2ndRgmntSecondBattalion.currentIndex() != 0:
            battalion_order = "Sixth Battalion"
            self.order_number = 5  # шестой по порядку батальон
            self.brgdSixthBattalionCostSetText = self.aBrgd2ndRgmntSecondBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBr2ndRgmntSecondBttlnModPushButton,
                                              self.aBrgd2ndRgmntSecondBattalion.currentText(), self.order_number)

    def a_the_seventh_bttln_mod_button_was_clicked(self):
        if self.aBrgd2ndRgmntThirdBattalion.currentIndex() != 0:
            battalion_order = "Seventh Battalion"
            self.order_number = 6  # седьмой по порядку батальон
            self.brgdSeventhBattalionCostSetText = self.aBrgd2ndRgmntThirdBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBr2ndRgmntThirdBttlnModPushButton,
                                              self.aBrgd2ndRgmntThirdBattalion.currentText(), self.order_number)
    def a_the_eighth_bttln_mod_button_was_clicked(self):
        if self.aBrgd2ndRgmntFourthBattalion.currentIndex() != 0:
            battalion_order = "Eighth Battalion"
            self.order_number = 7  # восьмой по порядку батальон
            self.brgdEighthBattalionCostSetText = self.aBrgd2ndRgmntFourthBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBr2ndRgmntFourthBttlnModPushButton,
                                              self.aBrgd2ndRgmntFourthBattalion.currentText(), self.order_number)



    def aBrgd1stRgmntAddBttryCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number, self.aBrgd1stRgmntAddBttryCost, self.aBrgdTotalCostView, 8, None, 0)





    def aBrgd2ndRgmntAddBttryCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number, self.aBrgd2ndRgmntAddBttryCost, self.aBrgdTotalCostView, 9, None, 0)









#     #--------------------------------------------------------------------------------------------------------------------

    def bttln_mod_button_was_clicked(self, battalion_order, brigade_number, mod_button_name, battalion_choosen_name, battalion_choosen_order):

        self.current_bttln_name_choosen = battalion_choosen_name # имя батальона который был выбран при нажатии окна МОД
        self.current_bttln_order_choosen = battalion_choosen_order # порядновый номер батальона в бригаде, который был выбран при нажатии окна МОД
        self.brigade_number = brigade_number #порядковый номер бригады
        self.bonus_window = BonusWindow()
        self.bonus_window.setWindowTitle(battalion_order)
        self.mod_button_name = mod_button_name

        self.bonuses = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]

        self.bonuses_list_in_window = [
            self.bonus_window.bonus1,
            self.bonus_window.bonus2,
            self.bonus_window.bonus3,
            self.bonus_window.bonus4,
            self.bonus_window.bonus5,
            self.bonus_window.bonus6,
            self.bonus_window.bonus7
        ]

        self.bonuses_checkboxes_in_window = [
            self.bonus_window.checkBox_1,
            self.bonus_window.checkBox_2,
            self.bonus_window.checkBox_3,
            self.bonus_window.checkBox_4,
            self.bonus_window.checkBox_5,
            self.bonus_window.checkBox_6,
            self.bonus_window.checkBox_7,
        ]

        checkbox_Action_list =[
            self.checkBox1_Action,
            self.checkBox2_Action,
            self.checkBox3_Action,
            self.checkBox4_Action,
            self.checkBox5_Action,
            self.checkBox6_Action,
            self.checkBox7_Action,
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

            # проводим проверку на ограничение бонусов определенного типа в бригаде
            if self.check_restriction_numer_of_bonus(self.brigade_number, self.btln_bonus_list[i]) == 0:
                self.bonuses_checkboxes_in_window[i].setDisabled(False)
            elif self.check_restriction_numer_of_bonus(self.brigade_number, self.btln_bonus_list[i]) == 1:
                self.bonuses_checkboxes_in_window[i].setDisabled(True)

            # текущий бонус уже есть в списке батальона , то отмечаем его
            if self.btln_bonus_list[i] in self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number):
                self.bonuses_checkboxes_in_window[i].setChecked(True)
                self.bonuses_checkboxes_in_window[i].setDisabled(False) # для бонусов с ограничением по количеству , снимает отключение выставленное  выше

                # проводим проверку на взаимоисключающие бонусы
                self.check_contradiction(self.btln_bonus_list[i], self.btln_bonus_list)


            self.bonuses_checkboxes_in_window[i].stateChanged.connect(checkbox_Action_list[i])

        self.bonus_window.ok_button.clicked.connect(self.ok_button_was_clicked)
        self.bonus_window.cancel_button.clicked.connect(self.cancel_button_was_clicked)

        self.bonus_window.show()

    def ok_button_was_clicked(self):
# gпроверка условия , что текущий выбор батальона тот же , что и при нажатии на кнопку модификации
        if self.presenter.BrigadeBttlnName(self.current_bttln_order_choosen, self.brigade_number) == self.current_bttln_name_choosen:

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
                case 7:
                    self.brgdEighthBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))



            # и обновляем полную стоимость бригады
            self.brgdTotalCostView()
            # перекрашиваем кнопку если надо
            self.check_bttln_bonus_for_button_color(self.order_number, self.brigade_number, self.mod_button_name)
            self.bonus_window.close()
        else:
            self.cancel_button_was_clicked()

    def cancel_button_was_clicked(self):
        self.bonus_window.close()

    def check_bttln_bonus_for_button_color(self, order_number, brigade_number, mod_button_name):
        # проводим проверку на наличие бонуса количество которых ограничено
        print("test0")
        bonus_list = self.presenter.BrigadeBttlnBonusList(order_number, brigade_number).copy()
        print (bonus_list)
        print("test1")


        for bonus in bonus_list:
            print("бонус", bonus, " ", self.check_restriction_numer_of_bonus(brigade_number, bonus))
            if self.check_restriction_numer_of_bonus(brigade_number, bonus) == 2:
                print("список бонусов до удаления")
                print(self.presenter.BrigadeBttlnBonusList(order_number, brigade_number))
                print("удаляем бонус из списка батальона")
                self.presenter.BrigadeBttlnBonusDel(bonus, order_number, brigade_number)
                print("список бонусов после удаления")
                print(self.presenter.BrigadeBttlnBonusList(order_number, brigade_number))
                print("запрашиваем стоимость бонус из списка бригады")
                bonus_cost  = self.presenter.BrigadeBonusCost(brigade_number, bonus)
                print (bonus_cost)

                self.presenter.BrigadeBttlnBonusCostAdd(bonus_cost * (-1), order_number, brigade_number)
                print("вычли стоимость из стоимости бонусов батальона")
            print(self.presenter.BrigadeBttlnBonusList(order_number, brigade_number))
        print("вышли из цикла")
        print(self.presenter.BrigadeBttlnBonusList(order_number, brigade_number))

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

    def checkBox4_Action(self):
        self.checkBox_Action(3)

    def checkBox5_Action(self):
        self.checkBox_Action(4)

    def checkBox6_Action(self):
        self.checkBox_Action(5)

    def checkBox7_Action(self):
        self.checkBox_Action(6)

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
        # если чекбокс отжат и такого бонуса нет, то показывается стоимость взятая из обьекта батальон
        else:
            if self.btln_bonus_list[order_number] in self.temporary_bonus_list:
                self.temporary_bonus_cost -= self.btln_bonus_cost_list[order_number]  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list[self.btln_bonus_list[order_number]]  # удаляем бонус из временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))

        self.check_contradiction(self.btln_bonus_list[order_number], self.btln_bonus_list)

    def check_contradiction(self, current_bonus, bonuses_list):
        if current_bonus == "Large":
            count = False
            position = 0
            for i in range (0, len(bonuses_list)):
                if bonuses_list[i] == "Small":
                    count = True
                    position = i
            if count:
                if self.bonuses_checkboxes_in_window[position].isEnabled():
                    self.bonuses_checkboxes_in_window[position].setDisabled(True)
                else:
                    self.bonuses_checkboxes_in_window[position].setDisabled(False)

        if current_bonus == "Small":
            count = False
            position = 0
            for i in range(0, len(bonuses_list)):
                if bonuses_list[i] == "Large":
                    count = True
                    position = i
            if count:
                if self.bonuses_checkboxes_in_window[position].isEnabled():
                    self.bonuses_checkboxes_in_window[position].setDisabled(True)
                else:
                    self.bonuses_checkboxes_in_window[position].setDisabled(False)

        if current_bonus == "Reliable, Elite 5+":
            count = False
            position = 0
            for i in range(0, len(bonuses_list)):
                if bonuses_list[i] == "Unreliable":
                    count = True
                    position = i
            if count:
                if self.bonuses_checkboxes_in_window[position].isEnabled():
                    self.bonuses_checkboxes_in_window[position].setDisabled(True)
                else:
                    self.bonuses_checkboxes_in_window[position].setDisabled(False)

        if current_bonus == "Unreliable":
            count = False
            position = 0
            for i in range(0, len(bonuses_list)):
                if bonuses_list[i] == "Reliable, Elite 5+":
                    count = True
                    position = i
            if count:
                if self.bonuses_checkboxes_in_window[position].isEnabled():
                    if self.check_restriction_numer_of_bonus(self.brigade_number, bonuses_list[position]) == 0:
                        self.bonuses_checkboxes_in_window[position].setDisabled(True)
                else:
                    if self.check_restriction_numer_of_bonus(self.brigade_number, bonuses_list[position]) != 1:
                        self.bonuses_checkboxes_in_window[position].setDisabled(False)


    def check_restriction_numer_of_bonus(self, brigade_number, current_btln_bonus):
        restricted_list = {"Reliable, Elite 5+": 2}
        result = -1
        if current_btln_bonus in restricted_list.keys():
            count = 0
            #запрос текущего списка бригады
            brigade_list = self.presenter.BrigadeCurrentList(brigade_number)
            # запрашиваем список бонусов каждого батальона и определяем суммарное колличество примененных бонусов
            print("-----------------")
            for order_number in range(0, len(brigade_list)):
                bttln_bonus_list = self.presenter.BrigadeBttlnBonusList(order_number, brigade_number)
                print(brigade_list[order_number].name)
                print(bttln_bonus_list)
                for current_bonus in bttln_bonus_list:
                    if current_bonus in restricted_list.keys():
                        count +=1
            print("count=", count)
            if count == restricted_list[current_btln_bonus]:
                result = 1
            elif count > restricted_list[current_btln_bonus]:
                result = 2
            else:
                result = 0

        return result

#     def saveFile(self):
#
#         fileName, _= QFileDialog.getSaveFileName(
#             parent=self,
#             caption='Select a data file',
#             filter='Data File (*.dat)'
#         )
#
#         if fileName:
#             try:
#                 with open(fileName, 'w') as fileToSave:
#                     fileToSave.write(self.dataCollectToSave())
#             except:
#                 self.error_message.show()
#         else:
#             pass
#
#     def dataCollectToSave(self):
#         dataSet= {"Side": self.country,
#                   "Division general": self.generalName.currentIndex()}
#         if self.aBrgdCmndr.currentIndex() != 0:
#             dataSet["1st Inf Brigade Commander"] = self.aBrgdCmndr.currentIndex()
#             dataSet["1st Inf Brigade 1st bttln"] = [self.aBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.a_brigade_number)]
#             dataSet["1st Inf Brigade 2nd bttln"] = [self.aBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.a_brigade_number)]
#             dataSet["1st Inf Brigade 3rd bttln"] = [self.aBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.a_brigade_number)]
#             dataSet["1st Inf Brigade 4th bttln"] = [self.aBrgdFourthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(3, self.a_brigade_number)]
#             dataSet["1st Inf Brigade add bttln"] = [self.aBrgdAdditionalBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(4, self.a_brigade_number)]
#             dataSet["1st Inf Brigade jgr add bttln"] = [self.aBrgdJgrAdditionalBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(5, self.a_brigade_number)]
#         if self.bBrgdCmndr.currentIndex() != 0:
#             dataSet["2nd Inf Brigade Commander"] = self.bBrgdCmndr.currentIndex()
#             dataSet["2nd Inf Brigade 1st bttln"] = [self.bBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.b_brigade_number)]
#             dataSet["2nd Inf Brigade 2nd bttln"] = [self.bBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.b_brigade_number)]
#             dataSet["2nd Inf Brigade 3rd bttln"] = [self.bBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.b_brigade_number)]
#             dataSet["2nd Inf Brigade 4th bttln"] = [self.bBrgdFourthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(3, self.b_brigade_number)]
#             dataSet["2nd Inf Brigade add bttln"] = [self.bBrgdAdditionalBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(4, self.b_brigade_number)]
#             dataSet["2nd Inf Brigade jgr add bttln"] = [self.bBrgdJgrAdditionalBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(5, self.b_brigade_number)]
#         if self.cBrgdCmndr.currentIndex() != 0:
#             dataSet["3rd Inf Brigade Commander"] = self.cBrgdCmndr.currentIndex()
#             dataSet["3rd Inf Brigade 1st bttln"] = [self.cBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.c_brigade_number)]
#             dataSet["3rd Inf Brigade 2nd bttln"] = [self.cBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.c_brigade_number)]
#             dataSet["3rd Inf Brigade 3rd bttln"] = [self.cBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.c_brigade_number)]
#             dataSet["3rd Inf Brigade 4th bttln"] = [self.cBrgdFourthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(3, self.c_brigade_number)]
#             dataSet["3rd Inf Brigade add bttln"] = [self.cBrgdAdditionalBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(4, self.c_brigade_number)]
#             dataSet["3rd Inf Brigade jgr add bttln"] = [self.cBrgdJgrAdditionalBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(5, self.c_brigade_number)]
#
#         if self.JgrBrgdCmndr.currentIndex() != 0:
#             dataSet["Jgr Brigade Commander"] = self.JgrBrgdCmndr.currentIndex()
#             dataSet["Jgr Brigade 1st bttln"] = [self.JgrBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.jgr_brigade_number)]
#             dataSet["Jgr Brigade 2nd bttln"] = [self.JgrBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.jgr_brigade_number)]
#             dataSet["Jgr Brigade 3rd bttln"] = [self.JgrBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.jgr_brigade_number)]
#             dataSet["Jgr Brigade 4th bttln"] = [self.JgrBrgdFourthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(3, self.jgr_brigade_number)]
#             dataSet["Jgr Brigade 5th bttln"] = [self.JgrBrgdFifthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(4, self.jgr_brigade_number)]
#             dataSet["Jgr Brigade 6th bttln"] = [self.JgrBrgdSixthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(5, self.jgr_brigade_number)]
#             dataSet["Jgr Brigade add1 bttln"] = [self.JgrBrgdAdditional1Battalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(6, self.jgr_brigade_number)]
#             dataSet["Jgr Brigade add2 bttln"] = [self.JgrBrgdAdditional2Battalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(7, self.jgr_brigade_number)]
#
#         if self.CombGrndrBrgdCmndr.currentIndex() != 0:
#             dataSet["Comb Grndr Brigade Commander"] = self.CombGrndrBrgdCmndr.currentIndex()
#             dataSet["Comb Grndr Brigade 1st bttln"] = [self.CombGrndrBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.comb_grndr_brigade_number)]
#             dataSet["Comb Grndr Brigade 2nd bttln"] = [self.CombGrndrBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.comb_grndr_brigade_number)]
#             dataSet["Comb Grndr Brigade 3rd bttln"] = [self.CombGrndrBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.comb_grndr_brigade_number)]
#             dataSet["Comb Grndr Brigade 4th bttln"] = [self.CombGrndrBrgdFourthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(3, self.comb_grndr_brigade_number)]
#             dataSet["Comb Grndr Brigade 5th bttln"] = [self.CombGrndrBrgdFifthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(4, self.comb_grndr_brigade_number)]
#             dataSet["Comb Grndr Brigade 6th bttln"] = [self.CombGrndrBrgdSixthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(5, self.comb_grndr_brigade_number)]
#             dataSet["Comb Grndr Brigade 7th bttln"] = [self.CombGrndrBrgdSeventhBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(6, self.comb_grndr_brigade_number)]
#
#         if self.GrndrBrgdCmndr.currentIndex() != 0:
#             dataSet["Grndr Brigade Commander"] = self.GrndrBrgdCmndr.currentIndex()
#             dataSet["Grndr Brigade 1st bttln"] = [self.GrndrBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.grndr_brigade_number)]
#             dataSet["Grndr Brigade 2nd bttln"] = [self.GrndrBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.grndr_brigade_number)]
#             dataSet["Grndr Brigade 3rd bttln"] = [self.GrndrBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.grndr_brigade_number)]
#             dataSet["Grndr Brigade 4th bttln"] = [self.GrndrBrgdFourthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(3, self.grndr_brigade_number)]
#
#         if self.LCvlryBrgdCmndr.currentIndex() != 0:
#             dataSet["L Cvlry Brigade Commander"] = self.LCvlryBrgdCmndr.currentIndex()
#             dataSet["L Cvlry Brigade 1st rgmnt"] = [self.LCvlryBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.light_cvlry_brigade_number)]
#             dataSet["L Cvlry Brigade 2nd rgmnt"] = [self.LCvlryBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.light_cvlry_brigade_number)]
#             dataSet["L Cvlry Brigade 3rd rgmnt"] = [self.LCvlryBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.light_cvlry_brigade_number)]
#
#         if self.HCvlryBrgdCmndr.currentIndex() != 0:
#             dataSet["H Cvlry Brigade Commander"] = self.HCvlryBrgdCmndr.currentIndex()
#             dataSet["H Cvlry Brigade 1st rgmnt"] = [self.HCvlryBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.heavy_cvlry_brigade_number)]
#             dataSet["H Cvlry Brigade 2nd rgmnt"] = [self.HCvlryBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.heavy_cvlry_brigade_number)]
#             dataSet["H Cvlry Brigade 3rd rgmnt"] = [self.HCvlryBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.heavy_cvlry_brigade_number)]
#
#         if self.CossackBrgdCmndr.currentIndex() != 0:
#             dataSet["Cossack Brigade Commander"] = self.CossackBrgdCmndr.currentIndex()
#             dataSet["Cossack Brigade 1st rgmnt"] = [self.CossackBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.cossack_brigade_number)]
#             dataSet["Cossack Brigade 2nd rgmnt"] = [self.CossackBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.cossack_brigade_number)]
#             dataSet["Cossack Brigade 3rd rgmnt"] = [self.CossackBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.cossack_brigade_number)]
#             dataSet["Cossack Brigade 4th rgmnt"] = [self.CossackBrgdFourthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(3, self.cossack_brigade_number)]
#             dataSet["Cossack Brigade 5th rgmnt"] = [self.CossackBrgdFifthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(4, self.cossack_brigade_number)]
#             dataSet["Cossack Brigade 6th rgmnt"] = [self.CossackBrgdSixthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(5, self.cossack_brigade_number)]
#
#         if self.ImpGrdInfBrgdCmndr.currentIndex() != 0:
#             dataSet["Imp Grd Inf Brigade Commander"] = self.ImpGrdInfBrgdCmndr.currentIndex()
#             dataSet["Imp Grd Inf Brigade 1st bttln"] = [self.ImpGrdInfBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.imp_grd_inf_brigade_number)]
#             dataSet["Imp Grd Inf Brigade 2nd bttln"] = [self.ImpGrdInfBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.imp_grd_inf_brigade_number)]
#             dataSet["Imp Grd Inf Brigade 3rd bttln"] = [self.ImpGrdInfBrgdThirdBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(2, self.imp_grd_inf_brigade_number)]
#             dataSet["Imp Grd Inf Brigade 4th bttln"] = [self.ImpGrdInfBrgdFourthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(3, self.imp_grd_inf_brigade_number)]
#             dataSet["Imp Grd Inf Brigade 5th bttln"] = [self.ImpGrdInfBrgdFifthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(4, self.imp_grd_inf_brigade_number)]
#             dataSet["Imp Grd Inf Brigade 6th bttln"] = [self.ImpGrdInfBrgdSixthBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(5, self.imp_grd_inf_brigade_number)]
#             dataSet["Imp Grd Inf Brigade add1 bttln"] = [self.ImpGrdInfBrgdAdditional1Battalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(6, self.imp_grd_inf_brigade_number)]
#             dataSet["Imp Grd Inf Brigade add2 bttln"] = [self.ImpGrdInfBrgdAdditional2Battalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(7, self.imp_grd_inf_brigade_number)]
#
#         if self.ImpGrdLCavBrgdCmndr.currentIndex() != 0:
#             dataSet["Imp Grd L Cav Brigade Commander"] = self.ImpGrdLCavBrgdCmndr.currentIndex()
#             dataSet["Imp Grd L Cav Brigade 1st rgmnt"] = [self.ImpGrdLCavBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.imp_grd_l_cav_brigade_number)]
#             dataSet["Imp Grd L Cav Brigade 2nd rgmnt"] = [self.ImpGrdLCavBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.imp_grd_l_cav_brigade_number)]
#
#         if self.ImpGrdHCavBrgdCmndr.currentIndex() != 0:
#             dataSet["Imp Grd H Cav Brigade Commander"] = self.ImpGrdHCavBrgdCmndr.currentIndex()
#             dataSet["Imp Grd H Cav Brigade 1st rgmnt"] = [self.ImpGrdHCavBrgdFirstBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(0, self.imp_grd_h_cav_brigade_number)]
#             dataSet["Imp Grd H Cav Brigade 2nd rgmnt"] = [self.ImpGrdHCavBrgdSecondBattalion.currentIndex(),
#                                                     self.presenter.BrigadeBttlnBonusList(1, self.imp_grd_h_cav_brigade_number)]
#
#         dataSet["Light Artillery Battery 1"] = [self.LightArtilleryBattery1.currentIndex()]
#         dataSet["Light Artillery Battery 2"] = [self.LightArtilleryBattery2.currentIndex()]
#         dataSet["Light Artillery Battery 3"] = [self.LightArtilleryBattery3.currentIndex()]
#         dataSet["Light Artillery Battery 4"] = [self.LightArtilleryBattery4.currentIndex()]
#         dataSet["Light Artillery Battery 5"] = [self.LightArtilleryBattery5.currentIndex()]
#         dataSet["Light Artillery Battery 6"] = [self.LightArtilleryBattery6.currentIndex()]
#
#         dataSet["Heavy Artillery Battery 1"] = [self.HeavyArtilleryBattery1.currentIndex()]
#         dataSet["Heavy Artillery Battery 2"] = [self.HeavyArtilleryBattery2.currentIndex()]
#         dataSet["Heavy Artillery Battery 3"] = [self.HeavyArtilleryBattery3.currentIndex()]
#         dataSet["Heavy Artillery Battery 4"] = [self.HeavyArtilleryBattery4.currentIndex()]
#
#         dataSet["Unicorn Battery 1"] = [self.UnicornBattery1.currentIndex()]
#         dataSet["Unicorn Battery 2"] = [self.UnicornBattery2.currentIndex()]
#         dataSet["Unicorn Battery 3"] = [self.UnicornBattery3.currentIndex()]
#         dataSet["Unicorn Battery 4"] = [self.UnicornBattery4.currentIndex()]
#         dataSet["Unicorn Battery 5"] = [self.UnicornBattery5.currentIndex()]
#         dataSet["Unicorn Battery 6"] = [self.UnicornBattery6.currentIndex()]
#
#         dataSet["Horse Artillery Battery 1"] = [self.HorseArtilleryBattery1.currentIndex()]
#         dataSet["Horse Artillery Battery 2"] = [self.HorseArtilleryBattery2.currentIndex()]
#         dataSet["Horse Artillery Battery 3"] = [self.HorseArtilleryBattery3.currentIndex()]
#
#         dataSet["EarthWorks 1"] = [self.EarthWorks1.currentIndex()]
#         dataSet["EarthWorks 2"] = [self.EarthWorks2.currentIndex()]
#
#
#
#         json_object = json.dumps(dataSet, indent=4)
#         return json_object
#
#     def loadData(self, data):
#
#         self.generalName.setCurrentIndex(data["Division general"])
#
#         if "1st Inf Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "1st Inf Brigade 1st bttln", 0, data["1st Inf Brigade 1st bttln"][0]+1, self.a_brigade_number)
#             # устанавливаеем командитра бригады
#             self.aBrgdCmndr.setCurrentIndex(data["1st Inf Brigade Commander"])
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "1st Inf Brigade 2nd bttln", 1, data["1st Inf Brigade 2nd bttln"][0], self.a_brigade_number)
#             # устанавливаеем батальон
#             self.aBrgdSecondBattalion.setCurrentIndex(data["1st Inf Brigade 2nd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "1st Inf Brigade 3rd bttln", 2, data["1st Inf Brigade 3rd bttln"][0], self.a_brigade_number)
#             self.aBrgdThirdBattalion.setCurrentIndex(data["1st Inf Brigade 3rd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "1st Inf Brigade 4th bttln", 3, data["1st Inf Brigade 4th bttln"][0], self.a_brigade_number)
#             self.aBrgdFourthBattalion.setCurrentIndex(data["1st Inf Brigade 4th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "1st Inf Brigade add bttln", 4, data["1st Inf Brigade add bttln"][0], self.a_brigade_number)
#             self.aBrgdAdditionalBattalion.setCurrentIndex(data["1st Inf Brigade add bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "1st Inf Brigade jgr add bttln", 5, data["1st Inf Brigade jgr add bttln"][0], self.a_brigade_number)
#             self.aBrgdJgrAdditionalBattalion.setCurrentIndex(data["1st Inf Brigade jgr add bttln"][0])
#
#         if "2nd Inf Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "2nd Inf Brigade 1st bttln", 0, data["2nd Inf Brigade 1st bttln"][0]+1, self.b_brigade_number)
#             self.bBrgdCmndr.setCurrentIndex(data["2nd Inf Brigade Commander"])
#
#             self.load_procedure_set_bonuses(data, "2nd Inf Brigade 2nd bttln", 1, data["2nd Inf Brigade 2nd bttln"][0], self.b_brigade_number)
#             self.bBrgdSecondBattalion.setCurrentIndex(data["2nd Inf Brigade 2nd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "2nd Inf Brigade 3rd bttln", 2, data["2nd Inf Brigade 3rd bttln"][0], self.b_brigade_number)
#             self.bBrgdThirdBattalion.setCurrentIndex(data["2nd Inf Brigade 3rd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "2nd Inf Brigade 4th bttln", 3, data["2nd Inf Brigade 4th bttln"][0], self.b_brigade_number)
#             self.bBrgdFourthBattalion.setCurrentIndex(data["2nd Inf Brigade 4th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "2nd Inf Brigade add bttln", 4, data["2nd Inf Brigade add bttln"][0], self.b_brigade_number)
#             self.bBrgdAdditionalBattalion.setCurrentIndex(data["2nd Inf Brigade add bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "2nd Inf Brigade jgr add bttln", 5, data["2nd Inf Brigade jgr add bttln"][0], self.b_brigade_number)
#             self.bBrgdJgrAdditionalBattalion.setCurrentIndex(data["2nd Inf Brigade jgr add bttln"][0])
#
#         if "3rd Inf Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "3rd Inf Brigade 1st bttln", 0, data["3rd Inf Brigade 1st bttln"][0]+1, self.c_brigade_number)
#             self.cBrgdCmndr.setCurrentIndex(data["3rd Inf Brigade Commander"])
#
#             self.load_procedure_set_bonuses(data, "3rd Inf Brigade 2nd bttln", 1, data["3rd Inf Brigade 2nd bttln"][0], self.c_brigade_number)
#             self.cBrgdSecondBattalion.setCurrentIndex(data["3rd Inf Brigade 2nd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "3rd Inf Brigade 3rd bttln", 2, data["3rd Inf Brigade 3rd bttln"][0], self.c_brigade_number)
#             self.cBrgdThirdBattalion.setCurrentIndex(data["3rd Inf Brigade 3rd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "3rd Inf Brigade 4th bttln", 3, data["3rd Inf Brigade 4th bttln"][0], self.c_brigade_number)
#             self.cBrgdFourthBattalion.setCurrentIndex(data["3rd Inf Brigade 4th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "3rd Inf Brigade add bttln", 4, data["3rd Inf Brigade add bttln"][0], self.c_brigade_number)
#             self.cBrgdAdditionalBattalion.setCurrentIndex(data["3rd Inf Brigade add bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "3rd Inf Brigade jgr add bttln", 5, data["3rd Inf Brigade jgr add bttln"][0], self.c_brigade_number)
#             self.cBrgdJgrAdditionalBattalion.setCurrentIndex(data["3rd Inf Brigade jgr add bttln"][0])
#
#         if "Jgr Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "Jgr Brigade 1st bttln", 0, data["Jgr Brigade 1st bttln"][0]+1, self.jgr_brigade_number)
#             self.load_procedure_set_bonuses(data, "Jgr Brigade 2nd bttln", 1, data["Jgr Brigade 2nd bttln"][0]+1, self.jgr_brigade_number)
#
#             self.JgrBrgdCmndr.setCurrentIndex(data["Jgr Brigade Commander"])
#
#             self.load_procedure_set_bonuses(data, "Jgr Brigade 3rd bttln", 2, data["Jgr Brigade 3rd bttln"][0], self.jgr_brigade_number)
#             self.JgrBrgdThirdBattalion.setCurrentIndex(data["Jgr Brigade 3rd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Jgr Brigade 4th bttln", 3, data["Jgr Brigade 4th bttln"][0], self.jgr_brigade_number)
#             self.JgrBrgdFourthBattalion.setCurrentIndex(data["Jgr Brigade 4th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Jgr Brigade 5th bttln", 4, data["Jgr Brigade 5th bttln"][0], self.jgr_brigade_number)
#             self.JgrBrgdFifthBattalion.setCurrentIndex(data["Jgr Brigade 5th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Jgr Brigade 6th bttln", 5, data["Jgr Brigade 6th bttln"][0], self.jgr_brigade_number)
#             self.JgrBrgdSixthBattalion.setCurrentIndex(data["Jgr Brigade 6th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Jgr Brigade add1 bttln", 6, data["Jgr Brigade add1 bttln"][0], self.jgr_brigade_number)
#             self.JgrBrgdAdditional1Battalion.setCurrentIndex(data["Jgr Brigade add1 bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Jgr Brigade add2 bttln", 7, data["Jgr Brigade add2 bttln"][0], self.jgr_brigade_number)
#             self.JgrBrgdAdditional2Battalion.setCurrentIndex(data["Jgr Brigade add2 bttln"][0])
#
#         if "Comb Grndr Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 1st bttln", 0, data["Comb Grndr Brigade 1st bttln"][0]+1, self.comb_grndr_brigade_number)
#             self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 2nd bttln", 1, data["Comb Grndr Brigade 2nd bttln"][0]+1, self.comb_grndr_brigade_number)
#
#             self.CombGrndrBrgdCmndr.setCurrentIndex(data["Comb Grndr Brigade Commander"])
#
#             self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 3rd bttln", 2, data["Comb Grndr Brigade 3rd bttln"][0], self.comb_grndr_brigade_number)
#             self.CombGrndrBrgdThirdBattalion.setCurrentIndex(data["Comb Grndr Brigade 3rd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 4th bttln", 3, data["Comb Grndr Brigade 4th bttln"][0], self.comb_grndr_brigade_number)
#             self.CombGrndrBrgdFourthBattalion.setCurrentIndex(data["Comb Grndr Brigade 4th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 5th bttln", 4, data["Comb Grndr Brigade 5th bttln"][0], self.comb_grndr_brigade_number)
#             self.CombGrndrBrgdFifthBattalion.setCurrentIndex(data["Comb Grndr Brigade 5th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 6th bttln", 5, data["Comb Grndr Brigade 6th bttln"][0], self.comb_grndr_brigade_number)
#             self.CombGrndrBrgdSixthBattalion.setCurrentIndex(data["Comb Grndr Brigade 6th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 7th bttln", 6, data["Comb Grndr Brigade 7th bttln"][0], self.comb_grndr_brigade_number)
#             self.CombGrndrBrgdSeventhBattalion.setCurrentIndex(data["Comb Grndr Brigade 7th bttln"][0])
#
#         if "Grndr Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "Grndr Brigade 1st bttln", 0, data["Grndr Brigade 1st bttln"][0]+1, self.grndr_brigade_number)
#             self.GrndrBrgdCmndr.setCurrentIndex(data["Grndr Brigade Commander"])
#
#             self.load_procedure_set_bonuses(data, "Grndr Brigade 2nd bttln", 1, data["Grndr Brigade 2nd bttln"][0], self.grndr_brigade_number)
#             self.GrndrBrgdSecondBattalion.setCurrentIndex(data["Grndr Brigade 2nd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Grndr Brigade 3rd bttln", 2, data["Grndr Brigade 3rd bttln"][0], self.grndr_brigade_number)
#             self.GrndrBrgdThirdBattalion.setCurrentIndex(data["Grndr Brigade 3rd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Grndr Brigade 4th bttln", 3, data["Grndr Brigade 4th bttln"][0], self.grndr_brigade_number)
#             self.GrndrBrgdFourthBattalion.setCurrentIndex(data["Grndr Brigade 4th bttln"][0])
#
#         if "L Cvlry Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "L Cvlry Brigade 1st rgmnt", 0, data["L Cvlry Brigade 1st rgmnt"][0]+1,self.light_cvlry_brigade_number)
#             self.LCvlryBrgdCmndr.setCurrentIndex(data["L Cvlry Brigade Commander"])
#             self.LCvlryBrgdFirstBattalion.setCurrentIndex(data["L Cvlry Brigade 1st rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "L Cvlry Brigade 2nd rgmnt", 1, data["L Cvlry Brigade 2nd rgmnt"][0], self.light_cvlry_brigade_number)
#             self.LCvlryBrgdSecondBattalion.setCurrentIndex(data["L Cvlry Brigade 2nd rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "L Cvlry Brigade 3rd rgmnt", 2, data["L Cvlry Brigade 3rd rgmnt"][0], self.light_cvlry_brigade_number)
#             self.LCvlryBrgdThirdBattalion.setCurrentIndex(data["L Cvlry Brigade 3rd rgmnt"][0])
#
#         if "H Cvlry Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "H Cvlry Brigade 1st rgmnt", 0, data["H Cvlry Brigade 1st rgmnt"][0]+1, self.heavy_cvlry_brigade_number)
#             self.HCvlryBrgdCmndr.setCurrentIndex(data["H Cvlry Brigade Commander"])
#             self.HCvlryBrgdFirstBattalion.setCurrentIndex(data["H Cvlry Brigade 1st rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "H Cvlry Brigade 2nd rgmnt", 1, data["H Cvlry Brigade 2nd rgmnt"][0], self.heavy_cvlry_brigade_number)
#             self.HCvlryBrgdSecondBattalion.setCurrentIndex(data["H Cvlry Brigade 2nd rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "H Cvlry Brigade 3rd rgmnt", 2, data["H Cvlry Brigade 3rd rgmnt"][0], self.heavy_cvlry_brigade_number)
#             self.HCvlryBrgdThirdBattalion.setCurrentIndex(data["H Cvlry Brigade 3rd rgmnt"][0])
#
#         if "Cossack Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "Cossack Brigade 1st rgmnt", 0, data["Cossack Brigade 1st rgmnt"][0]+1, self.cossack_brigade_number)
#             self.load_procedure_set_bonuses(data, "Cossack Brigade 2nd rgmnt", 1, data["Cossack Brigade 2nd rgmnt"][0]+1, self.cossack_brigade_number)
#             self.CossackBrgdCmndr.setCurrentIndex(data["Cossack Brigade Commander"])
#             self.CossackBrgdFirstBattalion.setCurrentIndex(data["Cossack Brigade 1st rgmnt"][0])
#             self.CossackBrgdSecondBattalion.setCurrentIndex(data["Cossack Brigade 2nd rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "Cossack Brigade 3rd rgmnt", 2, data["Cossack Brigade 3rd rgmnt"][0], self.cossack_brigade_number)
#             self.CossackBrgdThirdBattalion.setCurrentIndex(data["Cossack Brigade 3rd rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "Cossack Brigade 4th rgmnt", 3, data["Cossack Brigade 4th rgmnt"][0], self.cossack_brigade_number)
#             self.CossackBrgdFourthBattalion.setCurrentIndex(data["Cossack Brigade 4th rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "Cossack Brigade 5th rgmnt", 4, data["Cossack Brigade 5th rgmnt"][0], self.cossack_brigade_number)
#             self.CossackBrgdFifthBattalion.setCurrentIndex(data["Cossack Brigade 5th rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "Cossack Brigade 6th rgmnt", 5, data["Cossack Brigade 6th rgmnt"][0], self.cossack_brigade_number)
#             self.CossackBrgdSixthBattalion.setCurrentIndex(data["Cossack Brigade 6th rgmnt"][0])
#
#         if "Imp Grd Inf Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 1st bttln", 0, data["Imp Grd Inf Brigade 1st bttln"][0]+1, self.imp_grd_inf_brigade_number)
#             self.ImpGrdInfBrgdCmndr.setCurrentIndex(data["Imp Grd Inf Brigade Commander"])
#
#             self.ImpGrdInfBrgdFirstBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 1st bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 2nd bttln", 1, data["Imp Grd Inf Brigade 2nd bttln"][0], self.imp_grd_inf_brigade_number)
#             self.ImpGrdInfBrgdSecondBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 2nd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 3rd bttln", 2, data["Imp Grd Inf Brigade 3rd bttln"][0], self.imp_grd_inf_brigade_number)
#             self.ImpGrdInfBrgdThirdBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 3rd bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 4th bttln", 3, data["Imp Grd Inf Brigade 4th bttln"][0], self.imp_grd_inf_brigade_number)
#             self.ImpGrdInfBrgdFourthBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 4th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 5th bttln", 4, data["Imp Grd Inf Brigade 5th bttln"][0], self.imp_grd_inf_brigade_number)
#             self.ImpGrdInfBrgdFifthBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 5th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 6th bttln", 5, data["Imp Grd Inf Brigade 6th bttln"][0], self.imp_grd_inf_brigade_number)
#             self.ImpGrdInfBrgdSixthBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 6th bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade add1 bttln", 6, data["Imp Grd Inf Brigade add1 bttln"][0], self.imp_grd_inf_brigade_number)
#             self.ImpGrdInfBrgdAdditional1Battalion.setCurrentIndex(data["Imp Grd Inf Brigade add1 bttln"][0])
#
#             self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade add2 bttln", 7, data["Imp Grd Inf Brigade add2 bttln"][0], self.imp_grd_inf_brigade_number)
#             self.ImpGrdInfBrgdAdditional2Battalion.setCurrentIndex(data["Imp Grd Inf Brigade add2 bttln"][0])
#
#         if "Imp Grd L Cav Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "Imp Grd L Cav Brigade 1st rgmnt", 0, data["Imp Grd L Cav Brigade 1st rgmnt"][0]+1, self.imp_grd_l_cav_brigade_number)
#             self.ImpGrdLCavBrgdCmndr.setCurrentIndex(data["Imp Grd L Cav Brigade Commander"])
#
#             self.ImpGrdLCavBrgdFirstBattalion.setCurrentIndex(data["Imp Grd L Cav Brigade 1st rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "Imp Grd L Cav Brigade 2nd rgmnt", 1, data["Imp Grd L Cav Brigade 2nd rgmnt"][0], self.imp_grd_l_cav_brigade_number)
#             self.ImpGrdLCavBrgdSecondBattalion.setCurrentIndex(data["Imp Grd L Cav Brigade 2nd rgmnt"][0])
#
#         if "Imp Grd H Cav Brigade Commander" in data.keys():
#             # проверяем и устанавливаем бонусы батальона
#             self.load_procedure_set_bonuses(data, "Imp Grd H Cav Brigade 1st rgmnt", 0, data["Imp Grd H Cav Brigade 1st rgmnt"][0]+1, self.imp_grd_h_cav_brigade_number)
#             self.ImpGrdHCavBrgdCmndr.setCurrentIndex(data["Imp Grd H Cav Brigade Commander"])
#
#             self.ImpGrdHCavBrgdFirstBattalion.setCurrentIndex(data["Imp Grd H Cav Brigade 1st rgmnt"][0])
#
#             self.load_procedure_set_bonuses(data, "Imp Grd H Cav Brigade 2nd rgmnt", 1, data["Imp Grd H Cav Brigade 2nd rgmnt"][0], self.imp_grd_h_cav_brigade_number)
#             self.ImpGrdHCavBrgdSecondBattalion.setCurrentIndex(data["Imp Grd H Cav Brigade 2nd rgmnt"][0])
#
#         self.LightArtilleryBattery1.setCurrentIndex(data["Light Artillery Battery 1"][0])
#         self.LightArtilleryBattery2.setCurrentIndex(data["Light Artillery Battery 2"][0])
#         self.LightArtilleryBattery3.setCurrentIndex(data["Light Artillery Battery 3"][0])
#         self.LightArtilleryBattery4.setCurrentIndex(data["Light Artillery Battery 4"][0])
#         self.LightArtilleryBattery5.setCurrentIndex(data["Light Artillery Battery 5"][0])
#         self.LightArtilleryBattery6.setCurrentIndex(data["Light Artillery Battery 6"][0])
#
#         self.HeavyArtilleryBattery1.setCurrentIndex(data["Heavy Artillery Battery 1"][0])
#         self.HeavyArtilleryBattery2.setCurrentIndex(data["Heavy Artillery Battery 2"][0])
#         self.HeavyArtilleryBattery3.setCurrentIndex(data["Heavy Artillery Battery 3"][0])
#         self.HeavyArtilleryBattery4.setCurrentIndex(data["Heavy Artillery Battery 4"][0])
#
#         self.UnicornBattery1.setCurrentIndex(data["Unicorn Battery 1"][0])
#         self.UnicornBattery2.setCurrentIndex(data["Unicorn Battery 2"][0])
#         self.UnicornBattery3.setCurrentIndex(data["Unicorn Battery 3"][0])
#         self.UnicornBattery4.setCurrentIndex(data["Unicorn Battery 4"][0])
#         self.UnicornBattery5.setCurrentIndex(data["Unicorn Battery 5"][0])
#         self.UnicornBattery6.setCurrentIndex(data["Unicorn Battery 6"][0])
#
#         self.HorseArtilleryBattery1.setCurrentIndex(data["Horse Artillery Battery 1"][0])
#         self.HorseArtilleryBattery2.setCurrentIndex(data["Horse Artillery Battery 2"][0])
#         self.HorseArtilleryBattery3.setCurrentIndex(data["Horse Artillery Battery 3"][0])
#
#         self.EarthWorks1.setCurrentIndex(data["EarthWorks 1"][0])
#         self.EarthWorks2.setCurrentIndex(data["EarthWorks 2"][0])
#
#
#     def load_procedure_set_bonuses(self, data, bttln_name, place_in_br_list, order_in_bttln_list, brgd_number):
#         for bonus_name, v in data[bttln_name][1].items():
#             bonus_cost = 0
#             for i in range(0, len(self.presenter.BrigadeBonusNameList(brgd_number))):
#                 if bonus_name == self.presenter.BrigadeBonusNameList(brgd_number)[i]:
#                     bonus_cost = self.presenter.BrigadeBonusCostList(brgd_number)[i]
#             self.presenter.BrigadeBttlnListBonusAdd(bonus_name, place_in_br_list, order_in_bttln_list, brgd_number)
#             self.presenter.BrigadeBttlnListBonusCostAdd(bonus_cost, place_in_br_list, order_in_bttln_list, brgd_number)
#
#     def exportToPDF(self):
#
#         fileName, _= QFileDialog.getSaveFileName(
#             parent=self,
#             caption='Select a pdf file',
#             filter='Pdf File (*.pdf)'
#         )
#
#         if fileName:
#             try:
#                 self.dataToSavePdf(fileName)
#             except:
#                 self.error_message.text("pdf export error")
#                 self.error_message.show()
#         else:
#             pass
#
#
#
#     def dataToSavePdf(self, fileName):
#
#         pdf = FPDF(orientation="P", unit="mm", format="A4")
#         pdf.add_page()
#
#         pdf.add_font('FontNS', '', 'Fonts\\Noto Sans\\NotoSans-Regular.ttf')
#         pdf.add_font('FontNS', 'B', 'Fonts\\Noto Sans\\NotoSans-Bold.ttf')
#         pdf.add_font('FontNS', 'I', 'Fonts\\Noto Sans\\NotoSans-Italic.ttf')
#         pdf.add_font('FontNS', 'BI', 'Fonts\\Noto Sans\\NotoSans-BoldItalic.ttf')
#
#         pdf.set_font('FontNS', '', 8)
#         pdf.cell(10, 8, "Black Powder 2.0 Army Builder", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#         pdf.set_font('FontNS', 'B', 14)
#         pdf.cell(0, 8, "Imperial Russian Army Division list", align='C', new_x=XPos.LMARGIN)
#         pdf.set_font('FontNS', 'B', 10)
#         pdf.cell(0, 8, f'Total cost: {self.divisionTotalCost.text()}', align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#         self.print_line(pdf)
# # запрашиваем и печатаем имя, стоимость и умения дивиpионного командира
#         pdf.set_font('FontNS', 'I', 10)
#         pdf.cell(0, 8, "Division commander", new_x=XPos.LMARGIN)
#         pdf.cell(0, 8, "Cost", align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#         pdf.set_font('FontNS', 'B', 10)
#         pdf.cell(0, 8, f'{self.presenter.DivisionCmndrName(self.generalName.currentIndex())}', new_x=XPos.LMARGIN)
#         pdf.cell(0, 8, f'{self.presenter.DivisionCmndrCost(self.generalName.currentIndex())}', align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#         pdf.set_font('FontNS', '', 8)
#         pdf.multi_cell(0, 4, f'Skills: {self.presenter.DivisionCmndrSkills(self.generalName.currentIndex())}', new_x=XPos.LMARGIN,  new_y=YPos.NEXT)
#         self.print_line(pdf)
#         pdf.set_font('FontNS', 'I', 10)
#         pdf.cell(0, 8, "Cost", align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#
#
#         brigades_and_battalions = []
#         brigades_and_battalions.append(["Line Infantry Brigade", self.aBrgdCmndr, self.aBrgdTotalCost, self.a_brigade_number, 6])
#         brigades_and_battalions.append(["Line Infantry Brigade", self.bBrgdCmndr, self.bBrgdTotalCost, self.b_brigade_number, 6])
#         brigades_and_battalions.append(["Line Infantry Brigade", self.cBrgdCmndr, self.cBrgdTotalCost, self.c_brigade_number, 6])
#         brigades_and_battalions.append(["Jager Brigade", self.JgrBrgdCmndr, self.JgrBrgdTotalCost, self.jgr_brigade_number, 8])
#         brigades_and_battalions.append(["Combine Grenadier Brigade", self.CombGrndrBrgdCmndr, self.CombGrndrBrgdTotalCost, self.comb_grndr_brigade_number, 7])
#         brigades_and_battalions.append(["Grenadier Brigade", self.GrndrBrgdCmndr, self.GrndrBrgdTotalCost, self.grndr_brigade_number, 4])
#         brigades_and_battalions.append(["Light Cavalry Brigade", self.LCvlryBrgdCmndr, self.LCvlryBrgdTotalCost, self.light_cvlry_brigade_number, 3])
#         brigades_and_battalions.append(["Heavy Cavalry Brigade", self.HCvlryBrgdCmndr, self.HCvlryBrgdTotalCost, self.heavy_cvlry_brigade_number, 3])
#         brigades_and_battalions.append(["Cossack Brigade", self.CossackBrgdCmndr, self.CossackBrgdTotalCost, self.cossack_brigade_number, 6])
#         brigades_and_battalions.append(["Imperial Guard Infantry Brigade", self.ImpGrdInfBrgdCmndr, self.ImpGrdInfBrgdTotalCost, self.imp_grd_inf_brigade_number, 8])
#         brigades_and_battalions.append(["Imperial Guard Light Cavalry Brigade", self.ImpGrdLCavBrgdCmndr, self.ImpGrdLCavBrgdTotalCost, self.imp_grd_l_cav_brigade_number, 2])
#         brigades_and_battalions.append(["Imperial Guard Heavy Cavalry Brigade", self.ImpGrdHCavBrgdCmndr, self.ImpGrdHCavBrgdTotalCost, self.imp_grd_h_cav_brigade_number, 2])
#
#         for i in range (0, len(brigades_and_battalions)):
#            self.brigade_title_print(pdf, brigades_and_battalions[i][0], brigades_and_battalions[i][1], brigades_and_battalions[i][2], brigades_and_battalions[i][3], brigades_and_battalions[i][4], "Battalion")
#
#
#         artillery_presence = 0
#         for i in range (0, 19):
#             artillery_presence += self.presenter.BrigadeBttlnPresence(i, self.artillery_quasy_brigade_number)
#         if artillery_presence > 0:
#             self.print_line(pdf)
#             pdf.set_font('FontNS', 'B', 10)
#             pdf.cell(0, 8, 'Artillery', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#
#             for order_number in range(0, 19):
#                 if self.presenter.BrigadeBttlnName(order_number, self.artillery_quasy_brigade_number) != "empty":
#                     self.battalion_print(pdf, order_number, self.artillery_quasy_brigade_number, "Battery")
#
#         earthworks_presence = 0
#         for i in range (0, 2):
#             earthworks_presence += self.presenter.BrigadeBttlnPresence(i, self.earthworks_quasy_brigade_number)
#         if earthworks_presence > 0:
#             self.print_line(pdf)
#             pdf.set_font('FontNS', 'B', 10)
#             pdf.cell(0, 8, 'EarthWorks', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#
#             for order_number in range(0, 2):
#                 if self.presenter.BrigadeBttlnName(order_number, self.earthworks_quasy_brigade_number) != "empty":
#                     self.battalion_print(pdf, order_number, self.earthworks_quasy_brigade_number, 'EarthWorks')
#             self.print_line(pdf)
#
#         pdf.output(fileName)
#     def brigade_title_print(self, pdf, x_brigade_name, xBrgdCmndr, xBrgdTotalCost,x_brigade_number, number_of_battalions, flag):
#
#         # запрашиваем и печатаем (если выбран) имя и стоимость бригадного командира
#         if xBrgdCmndr.currentIndex() != 0:
#
#             pdf.set_font('FontNS', 'B', 10)
#             pdf.cell(0, 8, f'{x_brigade_name}', new_x=XPos.LMARGIN)
#             pdf.cell(0, 8, f'{xBrgdTotalCost.text()}', align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#             pdf.set_font('FontNS', 'I', 10)
#             pdf.cell(0, 8, f'Brigade Commander: ', new_x=XPos.END)
#             pdf.set_font('FontNS', '', 10)
#             pdf.cell(0, 8, f'{self.presenter.BrigadeCmndrsName(xBrgdCmndr.currentIndex(), x_brigade_number)}',
#                      new_x=XPos.LMARGIN)
#             pdf.cell(0, 8, f'{self.presenter.BrigadeCmndrsCost(xBrgdCmndr.currentIndex(), x_brigade_number)}',
#                      align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#
#             for order_number in range(0, number_of_battalions):
#                 # запрашиваем и печатаем имя , стоимость и бонусы  батальона (если он есть)
#                 if self.presenter.BrigadeBttlnName(order_number, x_brigade_number) != "empty":
#                     self.battalion_print(pdf, order_number, x_brigade_number, flag)
#
#
#     def print_line(self, pdf):
#         pdf.set_font('FontNS', '', 8)
#         line = "_" * 162
#         pdf.cell(0, 0, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#
#     def battalion_print (self, pdf, order_number, brigade_number, flag):
#         pdf.set_font('FontNS', 'I', 10)
#         pdf.cell(0, 8, f'{flag}: ', new_x=XPos.END)
#         pdf.set_font('FontNS', '', 10)
#         pdf.cell(0, 8, f'{self.presenter.BrigadeBttlnName(order_number, brigade_number)}', new_x=XPos.LMARGIN)
#         pdf.cell(0, 8, f'{self.presenter.BrigadeBttlnCost(order_number, brigade_number)}', align=Align.R,
#                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
#         if self.presenter.BrigadeBttlnBonusList(order_number, brigade_number):
#             pdf.set_font('FontNS', '', 8)
#             pdf.cell(0, 5, f'         Specials:  {self.presenter.BrigadeBttlnSpecials(order_number, brigade_number)}', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
