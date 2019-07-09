from playsound import playsound
import os

class Encoder: 
    def __init__(self):
        self.file_name = "x.wav"

    def encode(self, userCallsign, moduleCallsign, command): 

        # if linux 
        com = "echo -n '"+userCallsign+">"+moduleCallsign+":"+moduleCallsign+";"+command+"' | gen_packets -a 50 -o "+self.file_name+" -"

        os.system(com)
        playsound(self.file_name)

    def encode_with_message(self, userCallsign, moduleCallsign, command, message):
        # if linux 
        com = "echo -n '"+userCallsign+">"+moduleCallsign+":"+moduleCallsign+";"+command+"@@@"+message+"' | gen_packets -a 100 -o "+self.file_name+" -"

        os.system(com)
        playsound(self.file_name)

        
