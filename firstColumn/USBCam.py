from tkinter import *

class USBCam : 
    def __init__(self, main, column):
        self.main = main
        burstmode = LabelFrame(column, text="USB CAM", padx=10, pady=10)
        burstmode.grid(row=1, sticky="nwse") 

        captureBtn = Button(burstmode, text="CAPTURE", 
                width="10",
                height="5",
                command=self.capture) 
        captureBtn.grid(row=0)

    def capture(self):
        self.main.telecommand("CAPTURE") 
