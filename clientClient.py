
import socket
import threading



class Sender: #controller
    def __init__(self,window):
        self.window=window
        self.start = True
        self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketClient.connect(("192.168.1.5", 12800))
        self.msgReceivedDecoded = ""
        self.thread = threading.Thread(target=self.receivingThread,daemon=True)
        self.thread.start()

    def sendToStream(self, msg): #TODO: do the case if "fin"
        msgToSend = msg.encode()
        self.socketClient.send(msgToSend)


    def receivingThread(self):
        while True:
            msgReceived = self.socketClient.recv(1024)
            self.msgReceivedDecoded = msgReceived.decode()
            if self.msgReceivedDecoded[::-1][2::-1]=="fin":
                self.socketClient.close()
                break
            self.window.event_generate("<<MSG_RECEIVED>>")











