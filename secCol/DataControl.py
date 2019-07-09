from tkinter import * 
from collections import deque
class DataControl : 
    def __init__(self, main, column):
    
        self.main = main
        self.datePos = deque() 

        dataControl = LabelFrame(column,
                text="DATA CONTROL",
                padx=10,
                pady=10) 

        dataControl.grid(row=0,sticky="nwse")

        self.pof = Label(dataControl, text="POF > n/a")
        self.pof.grid(row=0, columnspan=2)

        getFifoBtn = Button(dataControl, 
                text="GET FIFO CONTENT",
                wraplength=80,
                justify=LEFT,
                width="10",
                height="5",
                command=self.getFifo)
        getFifoBtn.grid(row=1, column=0, pady=10)


        popAllBtn = Button(dataControl, 
                text="POP ALL",
                wraplength=80,
                justify=LEFT,
                width="10",
                height="5",
                command=self.popAll)

        popAllBtn.grid(row=1, 
                column=1,
                pady=10)
        '''        
        popSelected = Button(dataControl, 
                text="POP SELECTED",
                wraplength=80,
                justify=LEFT,
                width="10",
                height="5", 
                command=self.popSelected)
        popSelected.grid(row=2, column=0, pady=10)

        self.listbox = Listbox(dataControl, 
                selectmode="multiple")
        
        self.listbox.grid(row=0,
                column=1,
                rowspan=2,
                padx=10,
                pady=10)
        
        popSelected = Button(dataControl, 
                text="SELECT ALL",
                wraplength=80,
                justify=LEFT,
                width="10",
                height="3", 
                command=self.popSelected)
        popSelected.grid(row=2, column=1, pady=10)
        '''

    def getFifo(self): 
        self.main.telecommand("GETFIFOCONTENT")

    def popAll(self):
        self.main.telecommand("POPALL")

    def popSelected(self): 
        selected_text_list = [i for i in self.listbox.curselection()]
        selected_text_list = '@'.join(str(x) for x in selected_text_list)
        self.main.telecommand("POPSELECTED@@@"+selected_text_list)

    def addPacket(self, lenTxt, lenPic):
        text = "TXT : "+lenTxt+" PIC : "+lenPic
        self.pof.config(text="POF > "+text)
        
        '''
        bg='white'
        fg='black'
        last_index = self.listbox.size()
        s = '' 
        if packet=='T':
            s = 'TEXT'
        elif packet=='P' :
            s = 'PICTURE'
        else :
            # date
            bg='yellow'
            fg='black'
            s = packet
            self.datePos.append(last_index)

        self.listbox.insert(END, s)
        self.listbox.itemconfig(last_index, bg=bg, fg=fg)
        '''

    def selectAll(self): 
        total = self.listbox.size()
        for i in range(total): 
            if i not in self.datePos : 
                self.listbox.selection_set(i)
