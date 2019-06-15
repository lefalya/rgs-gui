from tkinter import * 
class DataControl : 
    def __init__(self, main, column):
    
        self.main = main
        
        dataControl = LabelFrame(column,
                text="DATA CONTROL",
                padx=10,
                pady=10) 

        dataControl.grid(row=0,sticky="nwse")

        getFifoBtn = Button(dataControl, 
                text="GET FIFO CONTENT",
                wraplength=80,
                justify=LEFT,
                width="10",
                height="5",
                command=self.getFifo)
        getFifoBtn.grid(row=0, column=0, pady=10)


        popAllBtn = Button(dataControl, 
                text="POP ALL",
                wraplength=80,
                justify=LEFT,
                width="10",
                height="5",
                command=self.popAll)

        popAllBtn.grid(row=1, 
                column=0,
                pady=10)
        
        popSelected = Button(dataControl, 
                text="POP SELECTED",
                wraplength=80,
                justify=LEFT,
                width="10",
                height="5", 
                command=self.popSelected)
        popSelected.grid(row=2, column=0, pady=10)

        listbox = Listbox(dataControl, 
                selectmode="multiple")
        
        listbox.grid(row=0,
                column=1,
                rowspan=2,
                padx=10,
                pady=10)

        ETTime = Label(dataControl, text="Estimated Transmission Time : ")
        ETTime.grid(row=2,column=1,
                padx=10,
                pady=10)

        for item in ["TEXT", "PICTURE", "ALT", "TEXT", "TEXT"]:
            listbox.insert(END, item)

    def getFifo(self): 
        self.main.telecommand("GETFIFOCONTENT")

    def popAll(self):
        self.main.telecommand("POPALL")

    def popSelected(self): 
        self.main.telecommand("POPSELECTED")
