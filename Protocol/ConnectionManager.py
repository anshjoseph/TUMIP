from typing import Dict, List
from threading import Thread
from .HeaderEval import DataProc
from random import randint
class Client:
    def __init__(self,manager,connection,address) -> None:
        
        self.l_range = 55000
        self.h_range = 60000
        self.stop = False
        self.index = None
        self.manager = manager
        while True:
            self.UDP_PORT = randint(self.l_range,self.h_range)
            if self.UDP_PORT not in self.manager.port:
                break
        self.size = 8
        self.dataProc = DataProc(self.UDP_PORT)
        self.connection = connection
        print(f"\tConnected by {address}")
        print(f"\tUDP PORT: {self.UDP_PORT}")
         
    def connect(self):
        while True:
            try:
                data = self.connection.recv(8024)
                if not data:
                    break
                ret = self.dataProc.Proc(data)
                self.connection.sendall(ret)
            except:
                self.disconnect()

    def disconnect(self):
        self.connection.close()

class Manager:
    def __init__(self) -> None:
        self.port = []
        self.thread = []
        self.__connection_dict:Dict[str:Client] = dict()
    def add(self,connection,address):
        client = Client(self,connection,address)
        th = Thread(target=client.connect) 
        client.index = len(self.thread)
        self.__connection_dict[str(address)] = client
        th.start()
        self.thread.append(th)
        
    def remove(self,addres):
        client:Client = self.__connection_dict[str(addres)]
        client.stop = True    
        self.thread.pop(client.index)
    def removeAll(self):
        for cl in self.__connection_dict:
            self.__connection_dict[cl].dataProc.stopUDP()
            self.__connection_dict[cl].disconnect()
        for th in self.thread:
            th.join()
        for th in self.thread:
            del th
        del self  