from tkinter import *
import time
import threading



window= Tk()
countVar = IntVar(value=1)
Label(window,textvariable = countVar).pack()


def count():
    while True:
        print("salut")
        time.sleep(2)
        window.event_generate("<<addUp>>")

def add(event):
    countVar.set(countVar.get()+1)

window.bind("<<addUp>>", add)
thread= threading.Thread(target=count)
thread.start()
window.mainloop()
