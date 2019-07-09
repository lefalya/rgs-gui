from tkinter import * 
from skyfield.api import load 
from datetime import datetime 
class TLE: 
    def __init__(self, main, column): 
        self.main = main 
        self.satellites = 'http://celestrak.com/NORAD/elements/ACTIVE.txt' 
        self.lapanA2 = load.tle(self.satellites)['LAPAN-A2']
        self.userEpoch = self.lapanA2.epoch
        
        ts = load.timescale() 
        t = ts.utc(datetime.utcnow().year,
                datetime.utcnow().month,
                datetime.utcnow().day,
                datetime.utcnow().hour,
                datetime.utcnow().minute,
                datetime.utcnow().second)
        days = t - self.userEpoch

        if abs(days) > 2: 
            self.satellites = load.tle(self.satellites, reload=True)['LAPAN-A2']
        
        self.activeTxt = open("ACTIVE.txt", "r") 
        self.TLE = self.activeTxt.readlines()
        self.lapanA2TLE = []
        
        # append TLE data from ACTIVE.txt
        self.lapanA2TLE.append(self.TLE[3084][:-1])
        self.lapanA2TLE.append(self.TLE[3085][:-1])
        self.lapanA2TLE.append(self.TLE[3086][:-1])

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

        self.moduleTLE = Label(tle, text="Module Epoch : ", anchor="w")
        self.moduleTLE.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self.selfTLE = Label(tle, text="Active.TXT Epoch : ", anchor="w") 
        self.selfTLE.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        self.sendTLEStatus = Label(tle, text="", anchor="w")
        self.sendTLEStatus.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        self.processTLEStatus = Label(tle, text="", anchor="w")
        self.processTLEStatus.grid(row=3, column=1, sticky="w", padx=10, pady=10)
        self.setActiveEpoch(self.userEpoch.utc_jpl())

    def getEpoch(self): 
        self.main.telecommand("GETEPOCH")

    def setActiveEpoch(self, dateStr): 
        self.selfTLE.config(text="Active.TXT Epoch : "+dateStr)
        self.selfTLE.config(wraplength=200)
    
    def showModEpoch(self, epoch):
        self.moduleTLE.config(text="Module Epoch : "+epoch)
        self.moduleTLE.config(wraplength=200)

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
        self.setNewTLESending() 
        self.main.telecommand_with_message(
                "TLE",
                tle)

    def setNewTLESending(self): 
        self.sendTLEStatus.config(text="SENDING")
        self.sendTLEStatus.config(background="orange")
        self.sendTLEStatus.config(fg="white")

    def setNewTLEReceived(self): 
        self.sendTLEStatus.config(text="RECEIVED")
        self.sendTLEStatus.config(background="green")
        self.sendTLEStatus.config(fg="white")
    
    def setNewTLEProcessing(self): 
        self.processTLEStatus.config(text="PROCESSING")
        self.processTLEStatus.config(background="orange")
        self.processTLEStatus.config(fg="white")
    
    def setNewTLEDone(self): 
        self.processTLEStatus.config(text="DONE")
        self.processTLEStatus.config(background="green")
        self.processTLEStatus.config(fg="white")

