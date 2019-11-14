import random
import sys
from threading import Thread, RLock
import socket
import time

class Listener(Thread):

    def __init__(self,socketClient):
        Thread.__init__(self)
        self.socketClient=socketClient
        self.started = True

    def run(self):
        while self.started:
            msgReceived = self.socketClient.recv(1024)
            print(msgReceived.decode())

