
class DataProc:
    def __init__(self) -> None:
        self.UDP_PORT = None
        
    def Proc(self,payload:bytes):
        header:bytes = payload[:10]
        data:bytes = payload[10:]