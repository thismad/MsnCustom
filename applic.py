##The only secure way I found to make Tkinter mix with threads is to never
##issue commands altering the graphical state of the application in another
##thread than the one where the mainloop was started. Not doing that often
##leads to random behaviour such as the one you have here. Fortunately, one
##of the commands that seems to work in secondary threads is event_generate,
##giving you a means to communicate between threads. If you have to pass
##information from one thread to another, you can use a Queue.
##
##This obviously complicates things a bit, but it may work far better.
##Please note that the 'when' option *must* be specified in the call to
##event_generate and *must not* be 'now'. If it's not specified or if it's
##'now', Tkinter may directly execute the binding in the secondary thread's
##context. (Eric Brunel)

import threading
import time
from tkinter import *
import queue

## Create main window
root = Tk()

## Communication queue
commQueue = queue.Queue()

## Function run in thread
def timeThread():
    curTime = 0
    while 1:
        ## Each time the time increases, put the new value in the queue...
        commQueue.put(curTime)
        ## ... and generate a custom event on the main window
        try:
            root.event_generate('<<TimeChanged>>', when='tail')
        ## If it failed, the window has been destoyed: over
        except TclError:
            break
        ## Next
        time.sleep(1)
        curTime += 1

## In the main thread, do usual stuff
timeVar = IntVar()
Label(root, textvariable=timeVar, width=8).pack()

## Use a binding on the custom event to get the new time value
## and change the variable to update the display
def timeChanged(event):
    timeVar.set(commQueue.get())

root.bind('<<TimeChanged>>', timeChanged)

## Run the thread and the GUI main loop
th=threading.Thread(target=timeThread)
th.start()

root.mainloop()