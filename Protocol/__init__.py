import socket

from ConnectionManager import Manager
class Server:
    def __init__(self,host:str,port:int):
        self.host = host
        self.port = port
        self.Manage = Manager()
        self.__serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def start(self):
        print(f"STARTING SERVER AT PORT NO: {self.port}")
        self.__serverTCP.bind((self.host,self.port))
        try:
            while True:
                self.__serverTCP.listen()
                conn, addr = self.__serverTCP.accept()
                with conn:
                    print(f"\t Connected by {addr}")
                    pass
                
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        print(f"\nSTOPING SERVER AT PORT NO: {self.port}")
        self.__serverTCP.close()


