from PyQt6 import QtWidgets
from view.LineInfantryBonusGuiWindow import Ui_LineInfanntryBonusWindow

class BonusWindow(QtWidgets.QMainWindow, Ui_LineInfanntryBonusWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(BonusWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)