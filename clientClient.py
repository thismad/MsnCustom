
import socket
import threading



class Sender: #controller
    def __init__(self,window):
        self.window=window
        self.start = True
        self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketClient.connect(("localhost", 12800))
        self.msgReceivedDecoded = ""
        self.thread = threading.Thread(target=self.receivingThread,daemon=True)
        self.thread.start()

    def sendToStream(self, msg): #TODO: do the case if "fin"
        msgToSend = msg.encode()
        self.socketClient.send(msgToSend)


    def receivingThread(self):
        while True:
            msgReceived = self.socketClient.recv(1024)
            self.msgReceivedDecoded = msgReceived
            if self.msgReceived.decode()=="fin":
                self.socketClient.close()
                break
            self.window.event_generate("<<MSG_RECEIVED>>")











