from PyQt6 import QtWidgets, uic
from view.StartGuiWindow import Ui_MainWindow
# from StartGuiWindow import Ui_MainWindow

class StartWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(StartWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)