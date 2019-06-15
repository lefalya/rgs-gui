from tkinter import *
from read_tle import read_tle 
from playsound import playsound
from firstColumn import LoopBackPanel
from firstColumn import USBCam
from firstColumn import TCPConnection

from secCol import DataControl
from secCol import TLE 

from thdCol import IncomingPackets

from module import Encoder 

import os
import serial 
import time 


class App:

    def __init__(self, master):

        self.userCallsign = ''
        self.moduleCallsign = ''
        self.encoder = Encoder()

        firstCol = Frame(master)
        secCol = Frame(master)
        thdCol = Frame(master)

        lpbckpnl    = LoopBackPanel(self, firstCol) 
        bustMode    = USBCam(self, firstCol) 
        bustMode    = TCPConnection(firstCol) 
    
        datCon      = DataControl(self, secCol) 
        tle         = TLE(self, secCol) 

        incPack     = IncomingPackets(thdCol)

        self.applySerial = False 
        self.serial = '' # blank object not null
       
        try :
            self.serial = serial.Serial(sys.argv[1])
            self.applySerial = True
        except:
            print('No serial connected')

        firstCol.grid(row=0, 
                column=0, 
                sticky='nswe',
                padx=20,
                pady=20)

        secCol.grid(row=0, 
                column=1, 
                sticky='nswe',
                padx=10,
                pady=20)
        
        thdCol.grid(row=0, 
                column=2, 
                sticky='nswe',
                padx=10,
                pady=20)

        if self.applySerial == True:
            self.serial.setRTS(False)
    
    def setCallsign(self, userCallsign, moduleCallsign): 
        self.userCallsign = userCallsign
        self.moduleCallsign = moduleCallsign

    def telecommand(self, command):
        if self.applySerial == True:
            self.serial.setRTS(True)
        time.sleep(0.5)
        
        if self.userCallsign != '' and self.moduleCallsign != '':  
            self.encoder.encode(self.userCallsign,
                    self.moduleCallsign,
                    command)
        else: 
            playsound('warning.wav')

        if self.applySerial == True: 
            self.serial.setRTS(False)

if __name__ == "__main__":
    root = Tk()
    root.title('RGS MISSION CONTROL CENTER')
    app = App(root)

    root.mainloop()
    root.destroy() # optional; see description below
