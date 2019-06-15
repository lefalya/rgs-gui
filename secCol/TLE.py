from tkinter import * 

class TLE: 
    def __init__(self, main, column): 
        self.main = main 

        tle = LabelFrame(column, 
                text="TLE",
                padx=10,
                pady=10)

        tle.grid(row=1,sticky="nswe")

        getEpoch = Button(tle, 
                text="GET EPOCH",
                wraplength=80, 
                justify=LEFT,
                width="10", 
                height="5") 
        getEpoch.grid(row=0,column=0,rowspan=2,pady=10)

        updtTLE = Button(tle, 
                text="UPDATE TLE",
                wraplength=80, 
                justify=LEFT,
                width="10", 
                height="5") 
        updtTLE.grid(row=2,rowspan=2,column=0)

        moduleTLE = Label(tle, text="Module Epoch : ", anchor="w")
        moduleTLE.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        selfTLE = Label(tle, text="Active.TXT Epoch : ", anchor="w") 
        selfTLE.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        self.sendTLEStatus = Label(tle, text=" SENDING ...", anchor="w")
        self.sendTLEStatus.grid(row=2, column=1, sticky="w", padx=10, pady=10)
        self.sendTLEStatus.config(background="yellow")

        self.processTLEStatus = Label(tle, text=" PROCESSING ...", anchor="w")
        self.processTLEStatus.grid(row=3, column=1, sticky="w", padx=10, pady=10)
        self.processTLEStatus.config(background="yellow")
