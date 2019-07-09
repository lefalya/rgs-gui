from tkinter import *

class IncomingPackets : 
    def __init__(self, column): 

        incPack = LabelFrame(column, 
                text="Message",
                padx=10,
                pady=10) 

        incPack.grid(row=0, sticky="nwse")

        self.listbox = Listbox(incPack,
                height=30)
        
        self.listbox.grid(row=0,
                padx=10,
                pady=10,
                sticky="nwse")
        
        if self.listbox.size() == 0 :
            self.addPacket('NO PACKET RECEIVED')

   
    def addPacket(self, packet):
        self.listbox.insert(END, packet) 
