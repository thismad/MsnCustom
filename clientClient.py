from threadPrinter import Listener
import socket

start = True
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketClient.connect(("localhost", 12800))
print("rentrez votre pseudo :")
pseudo = input()
listener = Listener(socketClient)
listener.start()

while start :
    entryMsg = input()
    msgToSend = pseudo + ": " + entryMsg
    socketClient.send(msgToSend.encode())
    if entryMsg == "fin":
        Listener.start = False
        start=False
        Listener.join()




socketClient.close()




