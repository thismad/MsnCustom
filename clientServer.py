import socket
import select
import re

connexionPrincipale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexionPrincipale.bind(("", 12800))
connexionPrincipale.listen((5))
serverLance = True
connectedSocketList = []

while serverLance :

    socketClients, wlist, xlist = select.select([connexionPrincipale],
                                                [], [], 0.05)

    for sockets in socketClients:
        connectedSocket, infosSocket = sockets.accept()
        connectedSocketList.append(connectedSocket)


    print("connected sockets : " + str(connectedSocketList))
    clientToRead = []
    receivedMsgList = []

    try:
        clientToRead, wlist, xlist = select.select(connectedSocketList, [], [], 0.05)
        print("client to read : " + str(clientToRead))

    except select.error:
        pass

    else:
        for i,client in enumerate(clientToRead):
            receivedMsg = (client.recv(1024))
            receivedMsgList.append(receivedMsg+b"\n")
            if receivedMsg == b"fin":
                serverLance = False

            for socket in connectedSocketList:
                for item in receivedMsgList:
                    socket.send(item)
            receivedMsgList.clear()
            print(receivedMsg.decode())

for sockets in connectedSocketList:
    sockets.close()
connexionPrincipale.close()




