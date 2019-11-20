from tkinter import *


class startFrame(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)

        self.window.bind("<Return>", self.clearField)
        self.entry = StringVar()
        self.pseudo = StringVar()
        self.pseudo.set("Choisissez votre pseudo!")
        Label(self, textvariable=self.pseudo).grid(row=0, column=0)
        Entry(self, textvariable=self.entry).grid(row=1, column=0)
        Button(self, text= "connect", command=lambda: controller.switchFrame()).grid(row=2, column=0)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.geometry("300*200")


    def clearField(self, event):
        self.entry.set("")
