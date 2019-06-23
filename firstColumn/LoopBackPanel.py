from tkinter import *

class LoopBackPanel : 
    def __init__(self, main, column): 

        loopback = LabelFrame(column, 
                text="MODULE", 
                padx=10, 
                pady=10)
        
        loopback.grid(row=0, sticky="nwse")
        
        callsign = Label(loopback, text="User Callsign")
        callsign.grid(row=0, sticky="w")
        
        self.main = main

        self.usrCall = Entry(loopback)

        self.usrCall.grid(row=1, 
                sticky="w") 
        
        modCallLbl = Label(loopback, text="RGS Callsign")
        modCallLbl.grid(row=2, sticky="w")
        
        self.modCall = Entry(loopback)

        self.modCall.grid(row=3, 
                sticky="w") 
        
        self.reachStatus = Label(loopback, text="NOT REACHED")
        self.reachStatus.grid(row=4, sticky="w")
        self.reachStatus.config(background="red")

        lpbckButton = Button(loopback, 
                text="LOOPBACK",
                width="10",
                height="5",
                command=self.loopBack)
        lpbckButton.grid(row=5, pady=10)
    
    def loopBack(self):
        self.main.setCallsign(
                self.usrCall.get(),
                self.modCall.get())

        self.main.telecommand("LOOPBACK")

    def setReached(self):
        self.reachStatus.config(text="REACHED")
        self.reachStatus.config(background="green")
        self.reachStatus.config(fg="white")

