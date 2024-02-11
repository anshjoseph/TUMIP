import socket
import os
from .ConnectionManager import Manager
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
class Server:
    def __init__(self,host:str,port:int):
        self.host = host
        self.port = port
        os.system(f"kill -9 $(lsof -ti tcp:{self.port})")
        self.Manage = Manager()
        self.__serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def start(self):
        
        self.__serverTCP.bind((self.host,self.port))
        print(f"STARTING SERVER AT PORT NO: {self.port}")
        try:
            while True:
                self.__serverTCP.listen()
                conn, addr = self.__serverTCP.accept()
                self.Manage.add(conn,addr)
                # conn.send(b"hellow ro")
                
                    
                
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        print(f"\nSTOPING SERVER AT PORT NO: {self.port}")
        self.Manage.removeAll()
        self.__serverTCP.close()
        


