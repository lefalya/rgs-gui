from tkinter import *

class IncomingPackets : 
    def __init__(self, column): 

        incPack = LabelFrame(column, 
                text="INCOMING PACKETS",
                padx=10,
                pady=10) 

        incPack.grid(row=0, sticky="nwse")

        listbox = Listbox(incPack)
        
        listbox.grid(row=0,
                padx=10,
                pady=10,
                sticky="nwse")

        for item in ["TEXT", 
                "PICTURE", 
                "ALT", 
                "TEXT", 
                "PICTURE", 
                "ALT", 
                "TEXT", 
                "TEXT",
                "PICTURE", 
                "ALT", 
                "TEXT", 
                "PICTURE", 
                "ALT", 
                "PICTURE", 
                "ALT", 
                "TEXT", 
                "TEXT"]: 
            listbox.insert(END, item)

