from tkinter import *

window = Tk()
window.geometry("200x200")
#create texts labels

pseudo=StringVar()
entry=StringVar()
pseudo.set("Choisissez votre pseudo !")

msg1=StringVar()
msg2=StringVar()
msg3=StringVar()

msg3.set("...")
msg2.set("...")
msg1.set("...")

def isOk():

    return True


pseudoLabel = Label(window,textvariable = pseudo)
label1 = Label(window,textvariable = msg1)
label2 = Label(window,textvariable = msg2)
label3 = Label(window,textvariable = msg3)
okcommand = window.register(isOk)
entryMsg = Entry(textvariable=entry, validate = "key", validatecommand = okcommand)

pseudoLabel.grid(row = 0,sticky ="wn")
label1.grid(row = 1, sticky = "w")
label2.grid(row = 2, sticky="w")
label3.grid(row =3,sticky = "w")
entryMsg.grid(row = 4, sticky ="w")



window.grid_columnconfigure(0, weight = 1)
window.grid_rowconfigure(0, weight = 1)

window.mainloop()



