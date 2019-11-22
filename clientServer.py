import socket
import select
import re
from Deserializer import Deserializer
from Serializer import Serializer

class Server:


    def __init__(self):
        self.connexionPrincipale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexionPrincipale.bind(("", 12800))
        self.connexionPrincipale.listen((5))
        self.serverLance = True
        self.connectedSocketList = []
        self.connectedDict ={}

    def startServer(self):
        while self.serverLance :

            socketClients, wlist, xlist = select.select([self.connexionPrincipale],
                                                        [], [], 0.05)

            for sockets in socketClients:
                connectedSocket, infosSocket = sockets.accept()
                self.connectedSocketList.append(connectedSocket)


            try:
                clientToRead, wlist, xlist = select.select(self.connectedSocketList, [], [], 0.05)


            except select.error:
                pass

            else:
                for client in clientToRead:
                    receivedMsg = (client.recv(1024))
                    self.handleSerial(receivedMsg, client)



    def handleSerial(self, receivedMsg, socketClient):
        """after receiving the message chose the task to do considering its prefix"""
        actionNb, msg = Deserializer.deserializeMsg(receivedMsg)

        if actionNb == Serializer.textEntry:
            self.sendMsgToAllSockets(receivedMsg)

        elif actionNb == Serializer.disconnected:
            self.sendMsgToAllSockets(receivedMsg) # if disconnection message, resend it to all the sockets so they can update their connected List
            del self.connectedDict[socketClient]
            socketClient.close()
            if not bool(self.connectedDict):
                self.serverLance = False
                self.connexionPrincipale.close()

        elif actionNb == Serializer.pseudo:
            self.connectedDict[socketClient] = msg
            self.updateClientsConnectedPseudos()


    def sendMsgToAllSockets(self, msg):
        """send the messages encoded to all the connected sockets """
        for socket in self.connectedSocketList:
            socket.send(msg)

    def updateClientsConnectedPseudos(self):
            pseudosListString = Serializer.serializePseudoList(self.connectedDict.values())
            self.sendMsgToAllSockets(pseudosListString)




serv = Server()
serv.startServer()




