
import socket
import threading
from PyQt5.QtCore import QObject, pyqtSignal
from Deserializer import Deserializer
from Serializer import Serializer

class Communicate(QObject):
    msgReceivedSignal = pyqtSignal()
    pseudoChangedSignal = pyqtSignal()

class Sender: #controller

    maxPersonsConnected = 3
    def __init__(self):
        self.start = True
        self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketClient.connect(("localhost", 12800))
        self.msgReceivedDecoded = ""
        self.pseudoConnectedList = [] #find a way to put "" in early labels but
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
        msgReceived = msgReceived.decode()
        sep = "0"
        msgReceivedList = [sep+x for x in msgReceived.split(sep)]
        for string in msgReceivedList:
            actionNb, msgDeserialized = Deserializer.deserializeMsg(string)

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
                    if not (pseud in self.pseudoConnectedList) and pseud != "": # split d'une string avec <pseudo>/ produit une liste à 2 entrées..
                        self.pseudoConnectedList.append(pseud)
                        self.c.pseudoChangedSignal.emit()








