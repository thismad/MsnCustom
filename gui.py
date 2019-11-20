from tkinter import *
import clientClient


class Afficheur():

    def __init__(self):
        ################################################## creating the view
        self.window = Tk()
        container = Frame(self.window)
        self.window.geometry("300x200")
        container.grid()
        container.grid_columnconfigure(0, weight=1)
        ################################################
        self.window.mainloop()

        # TODO modify here because it blocks everything after once it starts this loop. Lets make a new thread maybe
        # self.window.mainloop() # fais un thread et n'execute plus le reste du code..


class communicationFrame(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        # create texts labels
        self.window = master
        self.entry = StringVar()
        self.pseudo = StringVar()
        self.pseudoEntered = False

        # msgToSend to be received in clientClient
        # newEntry True if the user typed something new
        self._msgToSend = ""
        self.pseudo.set("Choisissez votre pseudo !")

        self.msg1 = StringVar(value="...")
        self.msg2 = StringVar(value="...")
        self.msg3 = StringVar(value="...")

        self.window.bind("<Return>", self.clearField)

        pseudoLabel = Label(self.window, textvariable=self.pseudo, font=("Courier",15),fg="red")
        label1 = Label(self.window, textvariable=self.msg1)
        label2 = Label(self.window, textvariable=self.msg2)
        label3 = Label(self.window, textvariable=self.msg3)
        entryMsg = Entry(textvariable=self.entry)

        pseudoLabel.grid(row=0, sticky="wn")
        label1.grid(row=1, sticky="w")
        label2.grid(row=2, sticky="w")
        label3.grid(row=3, sticky="w")
        entryMsg.grid(row=4, sticky="w")

        self.window.grid_columnconfigure(0, weight=3)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

        self.window.protocol("WM_DELETE_WINDOW", self._quitConfirm)
        self.window.bind("<<MSG_RECEIVED>>", self._changeTextLabels)

    def _quitConfirm(self):
        print("nous fermons la fenêtre et le socket associé")
        self.client.sendToStream("fin")  # notify the server that we end the communication
        self.window.destroy()

    def _changeTextLabels(self, event):
        self.msg1.set(self.msg2.get())
        self.msg2.set(self.msg3.get())
        self.msg3.set(self.client.msgReceivedDecoded)

    def clearField(self, event):
        self._msgToSend = self.entry.get()

        if not self.pseudoEntered:  # will execute only once if pseudo hasn't been entered yet
            self.pseudo.set(self.entry.get())
            self.pseudoEntered = True
        else:
            self._msgToSend = self.pseudo.get() + ": " + self._msgToSend
            self.client.sendToStream(self._msgToSend)

        self.entry.set("")

    def _getMsg(self):
        return self._msgToSend

    def _setMsg(self, newMsg):
        _msgToSend = newMsg

    def _getNewEntry(self):
        return self._newEntry

msgToSend = property(_getMsg, _setMsg)
newEntry = property(_getNewEntry)

