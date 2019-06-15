from playsound import playsound
import os

class Encoder: 

    def encode(self, userCallsign, moduleCallsign, command): 
        file_name = "x.wav" 

        # if linux 
        com = "echo -n '"+userCallsign+">"+moduleCallsign+":"+command+"' | gen_packets -a 100 -o "+file_name+" -"

        os.system(com)
        playsound(file_name)

