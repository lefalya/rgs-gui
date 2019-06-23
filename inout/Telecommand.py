class Telecommand : 
    def __init__(self, main): 
        self.main = main

    def parse(self,callsign,status,command): 
        self.main.incPack.addPacket(callsign+";"+
                status+";"+
                command) 
        self.execute(status,command) 
    
    def execute(self, status, command): 
        if status == '200': 
            if command == 'LOOPBACK':
                self.main.lpbckpnl.setReached()
