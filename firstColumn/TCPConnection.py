from tkinter import * 

class TCPConnection : 
    def __init__(self, column): 
        tcpConn = LabelFrame(column, text="TCP Connection", padx=5, pady=5) 
        tcpConn.grid(row=2)

        tcpEnable = Button(tcpConn, 
                text="ENABLE", 
                width="10",
                height="5") 
        tcpEnable.grid(row=0)

