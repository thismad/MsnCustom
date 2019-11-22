from PyQt5 import QtCore, QtGui, QtWidgets
from msnGUI import Ui_MainWindow
from clientClient import Sender

class Logic(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.switchPanel)
        self.pseudo=""
        self.lineEdit.editingFinished.connect(self.clearField)
        self.msgSender=""



    def switchPanel(self):
        if self.pseudo != "":
            self.stackedWidget.setCurrentIndex(1)

    def clearField(self):
        sender = self.sender()  # allow us to use one clearField for the 2 QlineEdit on bot stackedPanels
        if sender == self.lineEdit:
            if len(sender.text()) != 0:
                self.pseudo = sender.text()
                self.label.setText(sender.text())
        sender.setText("")

    def initConnection(self, window):
        self.msgSender = Sender()






app = QtWidgets.QApplication([])
logic=Logic()
logic.show()
app.exec_()
