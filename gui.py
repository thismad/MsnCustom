from tkinter import *


window = Tk()
cadre = Frame(window, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="top", fill=X)
window.mainloop()