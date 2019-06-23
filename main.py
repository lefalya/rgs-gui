from tkinter import *
from playsound import playsound

from firstColumn import LoopBackPanel
from firstColumn import USBCam
from firstColumn import TCPConnection
from secCol import DataControl
from secCol import TLE 
from thdCol import IncomingPackets

from module import Encoder 
from module import Direwolf

from inout import Telecommand

import os
import serial 
import time 
import threading

print_lock = threading.Lock()

class App:

    def __init__(self, master):

        self.userCallsign = ''
        self.moduleCallsign = ''
        self.encoder = Encoder()

        firstCol = Frame(master)
        secCol = Frame(master)
        thdCol = Frame(master)

        self.lpbckpnl    = LoopBackPanel(self, firstCol) 
        self.bustMode    = USBCam(self, firstCol) 
        self.bustMode    = TCPConnection(firstCol) 
    
        self.datCon      = DataControl(self, secCol) 
        self.tle         = TLE(self, secCol) 

        self.incPack     = IncomingPackets(thdCol)

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
        
        self.cparse = Telecommand(self)

        if self.applySerial == True:
            self.serial.setRTS(False)
    
    def recv_data(self): 
        while True : 
            receive = rx.receive()
            if receive.closed == True : 
                print_lock.release()
                break

            self.cparse.parse(receive.callsign, 
                    receive.status,
                    receive.message)

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
    
    def telecommand_with_message(self, command, message):
        if self.applySerial == True:
            self.serial.setRTS(True)
        time.sleep(0.5)
        
        if self.userCallsign != '' and self.moduleCallsign != '':  
            self.encoder.encode_with_message(self.userCallsign,
                    self.moduleCallsign,
                    command,
                    message)
        else: 
            playsound('warning.wav')

        if self.applySerial == True: 
            self.serial.setRTS(False)

if __name__ == "__main__":
    root = Tk()
    rx = Direwolf('localhost', 8001)
    root.title('RGS MISSION CONTROL CENTER')
    app = App(root)

    print_lock.acquire()
    p1 = threading.Thread(target=app.recv_data, args=())
    p1.start()
    root.mainloop()
    root.destroy() # optional; see description below
