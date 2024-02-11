import socket

class VideoFrame:
    def __init__(self,host,port) -> None:
        self.host = host
        self.port = port
        self.assign_address = ''
        self.window = 256*256
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    def start(self):
        self.sock.bind((self.host, self.port))
        print(f"\t\tUDP server for client {self.assign_address} is open at port {self.port}")
        while True:
            data, addr = self.sock.recvfrom(self.window) # buffer size is 1024 bytes
            print(data,addr)
            if addr == self.assign_address:
                print("received message: %s" % data)
        