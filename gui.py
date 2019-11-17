from tkinter import *
import clientClient


class Afficheur:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("200x200")

        # create texts labels
        self.entry=StringVar()
        self.pseudo=StringVar()

        # msgToSend to be received in clientClient
        # newEntry True if the user typed something new
        self._msgToSend = ""
        self._newEntry = False
        self.pseudo.set("Choisissez votre pseudo !")

        self.msg1 = StringVar(value="...")
        self.msg2 = StringVar(value="...")
        self.msg3 = StringVar(value="...")

        self.window.bind("<Return>", self.clearField)

        pseudoLabel = Label(self.window, textvariable=self.pseudo)
        label1 = Label(self.window, textvariable=self.msg1)
        label2 = Label(self.window, textvariable=self.msg2)
        label3 = Label(self.window, textvariable=self.msg3)
        labelEntry = Label(self.window, textvariable=self.entry)
        entryMsg = Entry(textvariable=self.entry)


        pseudoLabel.grid(row=0, sticky="wn")
        label1.grid(row=1, sticky="w")
        label2.grid(row=2, sticky="w")
        label3.grid(row=3, sticky="w")
        entryMsg.grid(row=4, sticky="w")
        labelEntry.grid(row=5)

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        print("salut")
        #TODO modify here because it blocks everything after once it starts this loop. Lets make a new thread maybe
        self.window.mainloop() # fais un thread et n'execute plus le reste du code..
        print("ok")

    def clearField(self,event):
        self._msgToSend = self.entry
        self._newEntry = True
        self.entry.set("")

    def _getMsg(self):
        self._newEntry = False  # when we fetch the newMsg newEntry is reseted
        return self._msgToSend

    def _setMsg(self, newMsg):
        _msgToSend = newMsg

    def _getNewEntry(self):
        return self._newEntry

    msgToSend = property(_getMsg, _setMsg)
    newEntry = property(_getNewEntry)











