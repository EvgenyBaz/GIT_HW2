
from PyQt6 import QtWidgets


from view.Error_message import Ui_Error_message

class MessageWindow(QtWidgets.QMainWindow, Ui_Error_message):
    def __init__(self, *args, obj=None, **kwargs):
        super(MessageWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Message:")
        self.OK_pushButton.clicked.connect((self.OK_clicked))

    def text(self, text):
        text = "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">"+text+"</span></p></body></html>"
        self.label.setWordWrap(True)
        self.label.setText(text)


    def OK_clicked(self):
        self.close()
