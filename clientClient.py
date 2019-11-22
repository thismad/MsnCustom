
import socket
import threading
from PyQt5.QtCore import QObject, pyqtSignal
from Deserializer import Deserializer
from Serializer import Serializer

class Communicate(QObject):
    msgReceivedSignal = pyqtSignal()
    pseudoChangedSignal = pyqtSignal()

class Sender: #controller
    def __init__(self):
        self.start = True
        self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketClient.connect(("192.168.1.36 ", 12800))
        self.msgReceivedDecoded = ""
        self.pseudoConnectedList = []
        self.c = Communicate()
        self.thread = threading.Thread(target=self.receivingThread,daemon=True)
        self.thread.start()

    def sendToStream(self, msg): #TODO: do the case if "fin"
        self.socketClient.send(msg)


    def receivingThread(self):
        while True:
            msgReceived = self.socketClient.recv(1024)
            self.handleSerial(msgReceived)



    def handleSerial(self, msgReceived):
        actionNb, msgDeserialized = Deserializer.deserializeMsg(msgReceived)

        if actionNb == Serializer.textEntry:
            self.msgReceivedDecoded = msgDeserialized
            self.c.msgReceivedSignal.emit()

        elif actionNb == Serializer.disconnected:
            self.pseudoConnectedList.remove(msgDeserialized)
            self.c.pseudoChangedSignal.emit()

        elif actionNb == Serializer.pseudoList:
            # separation caracter is '/' so we cut at this place
            newPseudoList = msgDeserialized.split('/')
            for pseud in newPseudoList:
                if pseud not in self.pseudoConnectedList:
                    self.pseudoConnectedList.append(pseud)
                    self.c.pseudoChangedSignal.emit()








