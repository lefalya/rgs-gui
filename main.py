from tkinter import *
from read_tle import read_tle 
import os
import serial 
import time 

class App:

    def __init__(self, master):

        frame = Frame(master)
        self.applySerial = False 
        self.serial = '' # blank object not null

        try :
            self.serial = serial.Serial(sys.argv[1])
            self.applySerial = True
        except:
            print('No serial connected')

        self.loopback = Button(frame, 
                text="LOOPBACK", 
                command=lambda : self.telecommand('loopback')).grid(row=0,
                        sticky='nwse', columnspan=2)

        self.getfifocontent = Button(frame, 
                text="GET FIFO CONTENT", 
                command=lambda : self.telecommand('getfifocontent')).grid(row=1,
                        sticky='nwse', columnspan=2)

        self.popall = Button(frame, 
                text="POP ALL",
                command=lambda : self.telecommand('popall')).grid(row=2,
                        sticky='nwse', columnspan=2)

        self.capture = Button(frame, 
                text="CAPTURE", 
                command=lambda : self.telecommand('capture')).grid(row=3,
                        sticky='nwse', columnspan=2)
        
        self.capture = Button(frame, 
                text="UPDATE TLE", 
                command=lambda : self.update_tle()).grid(row=4,
                        sticky='nwse', columnspan=2)
        
        self.target = Label(frame, 
                text='Target : ').grid(row=5, column=0)
        
        self.tgtStr = StringVar()
        self.targetEntry = Entry(frame,
                textvariable=self.tgtStr).grid(row=5, 
                column=1)
        
        self.groundSt = Label(frame, 
                text='Source : ').grid(row=6, column=0)
        
        self.gstStr = StringVar()
        self.gstEnt = Entry(frame,
                textvariable=self.gstStr).grid(row=6, 
                column=1)

        if self.applySerial == True:
            self.serial.setRTS(False)
        
        frame.pack()

    def telecommand(self, command):
        tgt = self.tgtStr.get()
        source = self.gstStr.get()

        if self.applySerial == True:
            self.serial.setRTS(True)
        time.sleep(0.5)

        self.generate_command(command=command, 
                tgt=tgt, 
                source=source)

        if self.applySerial == True: 
            self.serial.setRTS(False)

    def update_tle(self): 
        tle = read_tle()
        encoded_tle = tle.encode('active.txt') 
        tgt = self.tgtStr.get()
        source = self.gstStr.get()

        if self.applySerial == True:
            self.serial.setRTS(True)
 
        self.generate_command(command='utle', 
                tgt=tgt, 
                source=source,
                encoded=encoded_tle) 

        if self.applySerial == True: 
            self.serial.setRTS(False)

    def generate_command(self, **kwargs):
        p_command = kwargs['source']+">"+kwargs['tgt']+":"+kwargs['tgt']

        if kwargs['command'] == 'loopback': 
            p_command = p_command + ";LOOPBACK"
        elif kwargs['command'] == 'getfifocontent':
            p_command = p_command + ";GETFIFOCONTENT"
        elif kwargs['command'] == 'popall':
            p_command = p_command + ";POPALL"
        elif kwargs['command'] == 'capture':
            p_command = p_command + ";CAPTURE"
        elif kwargs['command'] == 'utle': 
            p_command = p_command + ";TLE#"+kwargs['encoded'] 
        
        self.send_command(p_command)

    def send_command(self, command): 
        os.system("echo -n '"+command+"' | gen_packets -a 25 -o x.wav - ")
        os.system('play x.wav')

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below
