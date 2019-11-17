from threadPrinter import Listener
import socket
import gui


class Sender:

    def __init__(self):
        self.start = True
        self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketClient.connect(("localhost", 12800))
        listener = Listener(self.socketClient)
        listener.start()
        self.graphicalInterface = gui.Afficheur()

        # we wait for the first entry to be entered by the user, it is considered as the pseudo
        while self.graphicalInterface.newEntry != True:
            pass
        self.pseudo = self.graphicalInterface.msgToSend # pseudo = newly entered input


    def run(self):
        while self.start :
            while self.graphicalInterface.newEntry != True: # why not create a listener type like java on the entry
                pass
            entryMsg = self.graphicalInterface.msgToSend
            msgToSend = self.pseudo + ": " + entryMsg
            print(msgToSend)
            self.socketClient.send(msgToSend.encode())
            if entryMsg == "fin":
                Listener.start = False
                self.start=False
                Listener.join()

        self.socketClient.close()





