class Telecommand : 
    def __init__(self, main): 
        self.main = main

    def parse(self,callsign,command): 
        if command != '':
            self.execute(callsign,command) 
    
    def execute(self, callsign, command): 

        # for command with message @@@
        if '@@@' in command : 
            command = command.split('@@@') 
            message = command[1]

            # FIFO related responses 
            if command[0] == "FIFOCONTENT":
                message = message.split('@')
                lenTxt = message[0]
                lenPic = message[1]
                self.main.datCon.addPacket(lenTxt,lenPic)
                '''
                if(len(message)%2==0):
                    for s in message :
                        # date
                        if '/' in s : 
                            self.main.datCon.addPacket(s)
                        else:
                            for i in s :
                                self.main.datCon.addPacket(i)
                '''

            # Module Epoch 
            elif command[0] == "MODEPOCH":
                self.main.tle.showModEpoch(message)
        
            # MSL responses
            elif command[0] == "MSL":
                self.main.incPack.addPacket(callsign+";"+
                        message) 

        # loopback response
        if command == 'LOOPBACK':
            self.main.lpbckpnl.setReached()           

        # TLE Response related 
        elif command == 'TLERECEIVED':
            self.main.tle.setNewTLEReceived() 
            self.main.tle.setNewTLEProcessing() 
        
        elif command == 'TLEDONE':
            self.main.tle.setNewTLEDone() 
             
