from tkinter import * 

class PAS: 
    def __init__(self, main, column): 
        self.main = main 
       
        pas = LabelFrame(column,
                text="CUSTOM MESSAGE",
                padx=10,
                pady=10)
        pas.grid(row=2,sticky="nswe")

        self.pasCommand = Entry(pas)
        self.pasCommand.grid(row=1,column=0)
    
        send = Button(pas,
                text="SEND",
                command=self.sendCommand)
        send.grid(row=2,column=0)

    def sendCommand(self):
        message = self.pasCommand.get() 
        self.main.telecommand_with_message('PAS',message)    
