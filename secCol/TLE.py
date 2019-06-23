from tkinter import * 
from skyfield.api import load 

class TLE: 
    def __init__(self, main, column): 
        self.main = main 
        self.satellites = 'http://celestrak.com/NORAD/elements/ACTIVE.txt' 
        self.lapanA2 = load.tle(self.satellites)['LAPAN-A2']
        self.userEpoch = self.lapanA2.epoch

        self.activeTxt = open("ACTIVE.txt", "r") 
        self.TLE = self.activeTxt.readlines()
        self.lapanA2TLE = []
        
        # append TLE data from ACTIVE.txt
        self.lapanA2TLE.append(self.TLE[3090][:-1])
        self.lapanA2TLE.append(self.TLE[3091][:-1])
        self.lapanA2TLE.append(self.TLE[3092][:-1])

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
                height="5", 
                command=self.getEpoch) 
        getEpoch.grid(row=0,column=0,rowspan=2,pady=10)

        updtTLE = Button(tle, 
                text="UPDATE TLE",
                wraplength=80, 
                justify=LEFT,
                width="10", 
                height="5",
                command=self.updateTLE) 
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

    def getEpoch(self): 
        self.main.telecommand("GETEPOCH")

    def encodeTLE(self): 
        output = [] 
        for line in self.lapanA2TLE : 
            li = line.split(' ')
            li = '/'.join(li)
            li = li.replace('\n', '')
            output.append(li)
        return ('%'.join(output))

    def updateTLE(self): 
        tle = self.encodeTLE()
        self.main.telecommand_with_message(
                "TLE",
                tle)
