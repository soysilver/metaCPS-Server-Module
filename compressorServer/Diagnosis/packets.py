from enum import Enum

class Packet:
    def __init__(self, pid):
        self.pid = pid

# 보낼 패킷의 형식 클라스
class SCShore(Packet):
    def __init__(self, rms=0.0, first = (" ",0.0), second=(" ",0.0), third = (" ",0.0), fourth= (" ",0.0), fifth = (" ",0.0)):
        super().__init__(pid = 6)
        self.rms = rms
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth