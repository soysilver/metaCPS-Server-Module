from enum import Enum

class Packet:
    def __init__(self, pid):
        self.pid = pid

# Enum to represent PacketType (simulating the PacketType enum in C#)
class PacketType(Enum):
    conn = 0
    SCStatus = 1
    SCOptData = 2
    CSOptData = 3
    CSStatus = 4
# Derived classes for different types of packets

class SCStatus(Packet):
    def __init__(self, pid=1, status=0):
        super().__init__(pid)
        self.status = status  # 0: idle, 1: busy

# Client-to-server packets

class CSOptData(Packet):
    def __init__(self, flowRate=0.0, pressure=0.0):
        super().__init__(PacketType.CSOptData)
        self.flowRate = flowRate
        self.pressure = pressure

class CSStatus(Packet):
    def __init__(self):
        super().__init__(PacketType.CSStatus)


class SCOptData(Packet):
    def __init__(self, pid=2, randFlowrate=0.0, randSP=0.0, randLengthOfSolution=0.0, 
                 randTotalPowerConsumption=0.0, optFlowrate=0.0, optSP=0.0, 
                 optLengthOfSolution=0.0, optTotalPowerConsumption=0.0, listBlowerIds=None):
        # 부모 클래스 Packet의 생성자를 호출
        super().__init__(pid)
        self.randFlowrate = randFlowrate
        self.randSP = randSP
        self.randLengthOfSolution = randLengthOfSolution
        self.randTotalPowerConsumption = randTotalPowerConsumption
        self.optFlowrate = optFlowrate
        self.optSP = optSP
        self.optLengthOfSolution = optLengthOfSolution
        self.optTotalPowerConsumption = optTotalPowerConsumption
        self.listBlowerIds = listBlowerIds if listBlowerIds is not None else []


class CSStatus(Packet):
    def __init__(self):
        super().__init__(PacketType.CSStatus)

# 보낼 패킷의 형식 클라스
class SCShore(Packet):
    def __init__(self, rms=0.0, first = 0.0, second=0.0, third = 0.0, fourth= 0.0, fifth = 0.0):
        super().__init__(pid = 6)
        self.rms = rms
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth