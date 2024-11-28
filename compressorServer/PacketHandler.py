import json
import combination


class PacketHandler:
    def __init__(self, server):
        self.server = server
        self.server.on_packet_data = self.on_packet_data

    # noinspection PyMethodMayBeStatic
    def on_packet_data(self, data, client):
        pkt = json.loads(data)
        if pkt:
            print("Received data:", data)
            print("Packet ID:", pkt['pid'])

            if pkt['pid'] == 3:  # asking for operation
                flowrate = pkt['flowRate']
                pressure = pkt['pressure']
                sc_pkt = combination.optimalOp(30, flowrate)

                str_pkt = json.dumps(sc_pkt.__dict__)  
                # 클라이언트에게만 응답
                #client.client_socket.sendall(str_pkt.encode('utf-8'))

            if pkt['pid'] == 4:  # asking for status
                sc_pkt = "{\"pid\":1, \"status\" 0}"
                str_pkt = json.dumps(sc_pkt)
                # 클라이언트에게만 응답
                #client.client_socket.sendall(str_pkt.encode('utf-8'))