
import socket 
import collections
from collections import deque

class Direwolf: 

    def __init__(self, host, port):
        self.connect_direwolf = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.connect_direwolf.connect((host, port)) 
    
    def receive(self): 
        connection_break = False
        buff = self.connect_direwolf.recv(1024) 
        if not buff:
            print('Connection Closed') 
            connection_break = True        

        buff = buff.decode('ISO-8859-1')
        buff = buff.split("\xf0")
        print(buff)
        buff = buff[1]
        buff = buff[0:(len(buff)-1)]
        
        # split[0] : date
        # split[1] : callsign
        # split[2] : status
        # split[3] : message

        buff = buff.split(';')
        callsign = buff[0] 
        status = buff[1] 
        message = buff[2]

        return_value = collections.namedtuple('receive_command',['callsign', 'status', 'message', 'closed']) 
        return return_value(callsign,status,message,connection_break)

