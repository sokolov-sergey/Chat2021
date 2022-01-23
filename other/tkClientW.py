import tkinter as tk
from tkinter import ttk


def sendMsg():
    msgList.insert(1,newMsg.get())

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
ttk.Entry(connFrame).grid(column=1, row=0)
ttk.Label(connFrame, text=':').grid(column=2, row=0)
ttk.Entry(connFrame, width=6).grid(column=3, row=0)
ttk.Button(connFrame, text='Connect').grid(column=4, row=0)
ttk.Label(connFrame, text='as', width=2).grid(column=5, row=0)
ttk.Entry(connFrame, width=20).grid(column=6, row=0)

usrFrame = tk.LabelFrame(MainW, text='Users', padx=10, pady=5)
usrFrame.columnconfigure(0,weight=100)
usrFrame.rowconfigure(0,weight=100)
usrFrame.grid(column=0, row=1, sticky='nswe')
tk.Listbox(usrFrame).grid(column=0, row=0, sticky='nswe')

#################################
msgFrame = tk.LabelFrame(MainW, text='Messages', padx=10, pady=5)
msgFrame.grid(column=1, row=1, sticky='nswe')
msgFrame.columnconfigure(0,weight= 90)
msgFrame.columnconfigure(1,weight= 20)
msgFrame.rowconfigure(0,weight= 90)
msgFrame.rowconfigure(1,weight= 10)

msgList = tk.Listbox(msgFrame)
msgList.grid(column=0, row=0, columnspan=2, sticky='nswe')
newMsg = ttk.Entry(msgFrame)
newMsg.grid(column=0,row=2,sticky='swe')

ttk.Button(msgFrame,text='send',command=sendMsg).grid(column=1,row=2,sticky='e')


MainW.mainloop()


