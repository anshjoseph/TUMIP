from typing import List
from threading import Thread
from HeaderEval import DataProc
from random import randint
class Client(Thread):
    def __init__(self,port_list,connection,address) -> None:
        self.dataProc = DataProc()
        self.l_range = 50000
        self.h_range = 60000
        while True:
            self.UDP_PORT = randint(self.l_range,self.h_range)
            if self.UDP_PORT not in port_list:
                break
        self.dataProc.UDP_PORT =  self.UDP_PORT
        self.size = 8
        self.connection = connection
        print(f"\tConnected by {address}")
         
    def connect(self):
        while True:
            self.connection = self.connection
            Data:bytes = self.connection.recv(1024*self.size)
            self.dataProc.Proc(Data)
    def disconnect(self):
        self.connection.close()

class Manager:
    def __init__(self) -> None:
        self.__port = []
        self.__connection_list:List[Client] = []
    def add(self,connection,address):
        pass