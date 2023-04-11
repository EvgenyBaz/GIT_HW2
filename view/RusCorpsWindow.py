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

        self.aBrFirstBttlnModPushButton.clicked.connect(self.the_first_bttln_mod_button_was_clicked)
        self.aBrSecondBttlnModPushButton.clicked.connect(self.the_second_bttln_mod_button_was_clicked)
        self.aBrThirdBttlnModPushButton.clicked.connect(self.the_third_bttln_mod_button_was_clicked)
        self.aBrFourthBttlnModPushButton.clicked.connect(self.the_fourth_bttln_mod_button_was_clicked)

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
        order_number = 0  # порядковое место в бригаде
        bttln_choosen_from_list = index  # индекс выбранного баталльона из списка
        self.presenter.rusLineInfantryBrigadeBttlnChoosen(order_number, bttln_choosen_from_list)
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
        total_cost = bttln1_cost + bttln2_cost + bttln3_cost + bttln4_cost + bttlnAdd_cost
        self.aBrgdTotalCost.setText(str(total_cost))

    def the_first_bttln_mod_button_was_clicked(self):

        if self.aBrgdFirstBattalion.currentIndex() != 0:
            battalion_order = "First Battalion"
            self.order_number = 0 # первый по порядку батальон
            self.current_bttln_index = self.aBrgdFirstBattalion.currentIndex() # имя батальона выбраного на данный момент

            self.bttln_mod_button_was_clicked(battalion_order)

    def the_second_bttln_mod_button_was_clicked(self):

        if self.aBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.current_bttln_index = self.aBrgdSecondBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.bttln_mod_button_was_clicked(battalion_order)

    def the_third_bttln_mod_button_was_clicked(self):

        if self.aBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.current_bttln_index = self.aBrgdThirdBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.bttln_mod_button_was_clicked(battalion_order)

    def the_fourth_bttln_mod_button_was_clicked(self):

        if self.aBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.current_bttln_index = self.aBrgdFourthBattalion.currentIndex()  # имя батальона выбраного на данный момент

            self.bttln_mod_button_was_clicked(battalion_order)

    def bttln_mod_button_was_clicked(self, battalion_order):
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

        if str(self.presenter.rusLineInfantryBrigadeBttlnName(self.order_number)) == "Line Infantry":
            # подготовка к выводу бонусов
            self.bonus_window.bonus1.setText("Veteran")
            self.bonus_window.bonus2.setText("Small")
            # гасим лишнюю опцию
            self.bonus_window.bonus3.close()
            self.bonus_window.checkBox_3.close()

            # print(self.presenter.rusLineInfantryBrigadeBttlnBonusList(0))

            # вводим проверку на наличие первого бонуса у батальона. Если есть то статус чекбокса - нажат
            if "Veteran" in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                self.bonus_window.checkBox_1.setChecked(True)
            self.bonus_window.checkBox_1.stateChanged.connect(self.checkBox1_Action)
            # вводим проверку на наличие второго бонуса у батальона. Если есть то статус чекбокса - нажат
            if "Small" in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                self.bonus_window.checkBox_2.setChecked(True)
            self.bonus_window.checkBox_2.stateChanged.connect(self.checkBox2_Action)

        self.bonus_window.ok_button.clicked.connect(self.ok_button_was_clicked)
        self.bonus_window.cancel_button.clicked.connect(self.cancel_button_was_clicked)
        self.bonus_window.show()

    def ok_button_was_clicked(self):
        # проверка - не переключил ли пользователь отряд , пока открыто окно выбора бонусов

        if self.current_bttln_index != 0:
        # if self.aBrgdFirstBattalion.currentIndex() != 0:
            # проверка если выбранный бонус не пуст то тогда применяются свойства бонууса.
            if self.bonus1 != "":
                # проверяем если чекбокс был нажат то добавляем свойста, если отжат , то удаляем свойства и стоимость
                if self.bonus_window.checkBox_1.isChecked():
                    # проверяем, если такой такого юонуса еще нет то добавляем
                    if "Veteran" not in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusAdd(self.bonus1, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus1_cost, self.order_number)
                else:
                    # проверяем, если такой бонус есть то удаляем
                    if "Veteran" in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusDel(self.bonus1, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus1_cost * (-1), self.order_number)
            # проверка если выбранный бонус 2 не пуст то тогда применяются свойства бонууса.
            if self.bonus2 != "":
                # проверяем если чекбокс был нажат то добавляем свойста, если отжат , то удаляем свойства и стоимость
                if self.bonus_window.checkBox_2.isChecked():
                    # проверяем, если такой такого юонуса еще нет то добавляем
                    if "Small" not in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusAdd(self.bonus2, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus2_cost, self.order_number)
                        print(self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number))
                else:
                    # проверяем, если такой бонус есть то удаляем
                    if "Small" in self.presenter.rusLineInfantryBrigadeBttlnBonusList(self.order_number):
                        self.presenter.rusLineInfantryBrigadeBttlnBonusDel(self.bonus2, self.order_number)
                        self.presenter.rusLineInfantryBrigadeBttlnBonusCostAdd(self.bonus2_cost * (-1), self.order_number)
            # печатаем в основном окне стоимости первого батальона новое значение
            match self.order_number:
                case 0:
                    self.aBrgdFirstBattalionCost.setText(str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))
                case 1:
                    self.aBrgdSecondBattalionCost.setText(str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))
                case 2:
                    self.aBrgdThirdBattalionCost.setText(str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))
                case 3:
                    self.aBrgdFourthBattalionCost.setText(str(self.presenter.rusLineInfantryBrigadeBttlnCost(self.order_number)))
            # и обновляем полную стоимость бригады
            self.aBrgdTotalCostView()

            self.bonus_window.close()
        else:
            self.cancel_button_was_clicked()

    def cancel_button_was_clicked(self):
        self.bonus_window.close()

    def checkBox1_Action(self):
        self.bonus1 = "Veteran"
        self.bonus1_cost = 8
        # проверка если чекбокс нажат и такого бонуса еще нет в списке бонусов батальона, то в окне отображения бонусов показывается стоимость с бонусом ()
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс нажат и такой бонус уже есть, то показывается стоимость взятая из обьекта батальон
        if self.bonus_window.checkBox_1.isChecked():
            if "Veteran" not in self.temporary_bonus_list:
                self.temporary_bonus_cost += self.bonus1_cost  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list["Veteran"] = None  # вносим бонус во временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
        # проверка если чекбокс отжат и такой бонус есть в списке бонусов батальона, то в окне отображения бонусов показывается стоимость за вычетом бонуса
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс отжат  и такого бонуса нет, то показывается стоимость взятая из обьекта батальон
        else:
            if "Veteran" in self.temporary_bonus_list:
                self.temporary_bonus_cost -= self.bonus1_cost  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list["Veteran"]  # удаляем бонус из временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))

    def checkBox2_Action(self):
        self.bonus2 = "Small"
        self.bonus2_cost = -8

        if self.bonus_window.checkBox_2.isChecked():
            if "Small" not in self.temporary_bonus_list:

                self.temporary_bonus_cost += self.bonus2_cost  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list["Small"] = None  # вносим бонус во временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
        else:
            if "Small" in self.temporary_bonus_list:

                self.temporary_bonus_cost -= self.bonus2_cost  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list["Small"]  # удаляем бонус из временный список

            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))

    def checkBox3_Action(self):
        self.bonus3 = "Sharpshooter"
        self.bonus3_cost = 3
