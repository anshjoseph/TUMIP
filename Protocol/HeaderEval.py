from threading import Thread
from multiprocessing import Process
from .VideoFrameUDP import VideoFrame

def RUN_UDP(port,host,allow):
    UDP_SERVER = VideoFrame(host,port)
    UDP_SERVER.assign_address = allow
    UDP_SERVER.start()
class DataProc:
    def __init__(self,UDP_PORT) -> None:
        self.UDP_PORT:int = UDP_PORT
        self.__process = Process(target=RUN_UDP,args=(self.UDP_PORT,'0.0.0.0','127.0.0.1'))
    def startUDP(self):
        self.__process.start()
    def stopUDP(self):
        self.__process.kill()
    def Proc(self,payload:bytes)->bytes:
        header:bytes = int.from_bytes(payload[:9],'big')
        self.user_id = header >> 32 & 2**32 -1
        self.req,self.flag,self.com = (header & 2**32-1) >> 24  ,((header & 2**32-1) >> 16) & 2**8 - 1, (header & 2**32-1) & 2**16 - 1
        self.data:bytes = payload[9:]
        return self.des().to_bytes(9,'big')
    def des(self)->int:
        if self.req == 1 and self.flag == 0:
            data = 1 << 64
            data1 = data | 32 << 32
            data2 = data1 | 1 << 24
            data3 = data2 | 0 << 16
            data4 = data3 | self.UDP_PORT
            payload = data4
            self.startUDP()
            return payload
        elif self.req == 2 and self.flag == 1:
            pass
        elif self.req == 3 and self.flag == 0:
            pass
        return 0