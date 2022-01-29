from os import error
import tkinter as tk
from tkinter import ttk
import threading
import time
import client
from socket import socket

ServerSocket: socket


def sendMsg():
    global ServerSocket
    msg = newMsg.get()
    client.sendToServer(msg, ServerSocket)
    log(msg)


def log(str):
    msgList.insert(0, str)


def connectToServer():
    global ServerSocket
    try:
        addr = srvAddrEntry.get()
        port = srvPortEntry.get()
        username = usernameEntry.get()
        ServerSocket = client.connect(addr, port, username)
        if ServerSocket == False:
            log('Error:could not connect to Server')
        else:
            log('Connected')
    except error as err:
        log('Error:'+err.strerror)


#####################################

MainW = tk.Tk()
MainW.title('CH 2021')
MainW.geometry("600x700+100+100")
MainW.columnconfigure(0, weight=20)
MainW.columnconfigure(1, weight=80)
MainW.rowconfigure(0, weight=5)
MainW.rowconfigure(1, weight=95)

connFrame = tk.LabelFrame(MainW, text='Connect',
                          padx=10, pady=5)
connFrame.grid(columnspan=3, row=0, sticky='nswe')
ttk.Label(connFrame, text='Server').grid(column=0, row=0)
srvAddrEntry = ttk.Entry(connFrame)
srvAddrEntry.grid(column=1, row=0)
srvAddrEntry.insert(0, '192.168.1.100')

ttk.Label(connFrame, text=':').grid(column=2, row=0)
srvPortEntry = ttk.Entry(connFrame, width=6)
srvPortEntry.grid(column=3, row=0)
srvPortEntry.insert(0, '12345')


ttk.Button(connFrame, text='Connect',
           command=connectToServer).grid(column=4, row=0)
ttk.Label(connFrame, text='as', width=2).grid(column=5, row=0)
usernameEntry = ttk.Entry(connFrame, width=20)
usernameEntry.grid(column=6, row=0)

usrFrame = tk.LabelFrame(MainW, text='Users', padx=10, pady=5)
usrFrame.columnconfigure(0, weight=100)
usrFrame.rowconfigure(0, weight=100)
usrFrame.grid(column=0, row=1, sticky='nswe')
tk.Listbox(usrFrame, bg='#D0F3A7').grid(column=0, row=0, sticky='nswe')

#################################
msgFrame = tk.LabelFrame(MainW, text='Messages', padx=10, pady=5)
msgFrame.grid(column=1, row=1, sticky='nswe')
msgFrame.columnconfigure(0, weight=90)
msgFrame.columnconfigure(1, weight=20)
msgFrame.rowconfigure(0, weight=90)
msgFrame.rowconfigure(1, weight=10)

msgList = tk.Listbox(msgFrame, bg='#9CCAC2')
msgList.grid(column=0, row=0, columnspan=2, sticky='nswe')
newMsg = ttk.Entry(msgFrame)
newMsg.grid(column=0, row=2, sticky='swe')

btnSend = ttk.Button(msgFrame, text='send', command=sendMsg)
btnSend.grid(column=1, row=2, sticky='e')


##################################

def autoSend():
    return
    try:
        while True:
            msgList.insert(0, time.strftime("%H:%M:%S"))
            time.sleep(1)
    except:
        pass


tr = threading.Thread(target=autoSend)
tr.start()

MainW.mainloop()

print("!!! exit")
