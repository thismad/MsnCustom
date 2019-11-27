from PyQt5 import QtCore, QtGui, QtWidgets
from msnGUI import Ui_MainWindow
from clientClient import Sender
from Serializer import Serializer

class Logic(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.switchPanel)
        self.pseudo=""
        self.lineEdit.editingFinished.connect(self.clearField)
        self.msgSender=""
        self.lineEdit_2.editingFinished.connect(self.sendMsgToServer)


    def closeEvent(self, event):
        """ if msgSender isnt initiated, close the program (thread not running in Sender), else send the disconnection signal to Thread and server"""
        if self.msgSender=="":
            event.accept()
        else :
            self.msgSender.sendToStream(Serializer.serializeDisconnection(self.pseudo))


    def switchPanel(self):
        if self.pseudo != "":
            self.stackedWidget.setCurrentIndex(1)
            self.initConnection()

    def clearField(self):
        sender = self.sender()  # allow us to use one clearField for the 2 QlineEdit on bot stackedPanels
        if sender == self.lineEdit:
            if len(sender.text()) != 0:
                self.pseudo = sender.text()
                self.label.setText(sender.text())
        sender.setText("")

    def initConnection(self):
        self.msgSender = Sender()
        pseudoSerialized = Serializer.serializePseudo(self.pseudo)
        self.msgSender.sendToStream(pseudoSerialized)
        self.msgSender.c.msgReceivedSignal.connect(self.reactToReceivedMsg) # try to do better if it works
        self.msgSender.c.pseudoChangedSignal.connect(self.reactToPseudosConnected)


    def sendMsgToServer(self):
        msgSerialized = Serializer.serializeTextEntry(self.pseudo + ": " +self.lineEdit_2.text())
        self.msgSender.sendToStream(msgSerialized)
        self.clearField()

    def reactToReceivedMsg(self):
        self.label_2.setText(self.label_3.text())
        self.label_3.setText(self.label_4.text())
        self.label_4.setText(self.label_5.text())
        self.label_5.setText((self.label_6.text()))
        self.label_6.setText(self.msgSender.msgReceivedDecoded)

    def reactToPseudosConnected(self):
        lenghtOfPseudoList = len(self.msgSender.pseudoConnectedList)
        if lenghtOfPseudoList !=0:
            self.label_7.setText(self.msgSender.pseudoConnectedList[0])

        if lenghtOfPseudoList > 1:
            self.label_8.setText(self.msgSender.pseudoConnectedList[1])
        else :
            self.label_8.setText("")

        if lenghtOfPseudoList > 2:
            self.label_9.setText(self.msgSender.pseudoConnectedList[2])
        else :
            self.label_9.setText("")







app = QtWidgets.QApplication([])
logic=Logic()
logic.show()
app.exec_()
