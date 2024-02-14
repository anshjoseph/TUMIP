import socket
import uuid
import numpy as np
import os

class VideoFrame:
    def __init__(self,host,port) -> None:
        self.host = host
        self.port = port
        self.assign_address = ''
        self.window = 196773 * 8 * 100
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    def start(self):
        self.sock.bind((self.host, self.port))
        print(f"\t\tUDP server for client {self.assign_address} is open at port {self.port}")
        while True:
            data, addr = self.sock.recvfrom(self.window) # buffer size is 1024 bytes
            print("data")
            
            with open(f"{uuid.uuid4()}.jpg",'wb') as file:
                file.write(data)
            # data = pickle.loads(data)
            # if addr == self.assign_address:
            #     print("received message: %s" % data)
        