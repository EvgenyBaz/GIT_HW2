from PyQt6 import QtWidgets
from view.BonusGuiWindow import Ui_BonusWindow

class BonusWindow(QtWidgets.QMainWindow, Ui_BonusWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(BonusWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)