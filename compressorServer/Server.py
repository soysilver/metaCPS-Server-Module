import socket
import threading
import packets
import json
import combination
import multiComb
from Diagnosis import shore
from PacketHandler import PacketHandler


class Server:
    def __init__(self, ip='0.0.0.0', port=7777):
        self.ip = ip
        self.port = port
        self.makepct = packets.SCStatus()

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(10)
        print(f"Server started on {self.ip}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address} has been established.")

            client_thread = threading.Thread(target=Server.handle_client, args=(client_socket, self,))
            client_thread.start()

    def broadcast(data, client_socket, self):

        try:
            pkt = json.loads(data)
            if pkt:
                print("Received data:", data)
                print("Packet ID:", pkt['pid'])
                sc_pkt = '{"pid":0}'
                if pkt['pid'] == 3:  # asking for operation
                    flowrate = pkt['flowRate']
                    pressure = int(pkt['pressure'])
                    if 0< pressure <=50 and pressure != 25:
                        sc_pkt = combination.optimalOp(pressure, flowrate)
                    else: sc_pkt = multiComb.optimalOp(25, flowrate) 
                    str_pkt = json.dumps(sc_pkt.__dict__)
                if pkt['pid'] == 4:  # asking for status
                    sc_pkt = self.makepct
                    str_pkt = json.dumps(sc_pkt.__dict__)
                if pkt['pid'] == 5:  # asking for operation
                    SCC = packets.SCShore()
                    sc_pkt = shore.Shore(SCC, pkt)
                    str_pkt = json.dumps(sc_pkt.__dict__)
                totalsent = 0
                while totalsent< len(str_pkt):
                    print("sending "+str_pkt)
                    sent = client_socket.send(str_pkt.encode('ascii'))

                    print(sent)
                    totalsent = totalsent + sent
                    print("sent "+str_pkt)
                    
        except Exception as e:
            print(f"Error sending data to client: {e}") 
            client_socket.close()


    def handle_client(client_socket, self):
        while True:
            data = client_socket.recv(1024)
            if not data:
                print(f"Conn dead")
                break  # 클라이언트가 연결을 종료하면 루프 종료
            print("Data received:", data)
            if (json.loads(data)['pid']):
                Server.broadcast(data, client_socket, self)

    def stop_server(self):
        self.server_started = False
        self.server_socket.close()
        print("Server stopped")


def start_server(port):
    server = Server(port=port)
    packet_handler = PacketHandler(server)
    
    def on_client_enter(count):
        print(f"Client connected. Total clients: {count}")

    server.on_client_enter = on_client_enter
    server.on_packet_data = packet_handler.on_packet_data

    server.start_server()

    try:
        while True:
            pass  # 서버가 계속 실행되도록 유지
    except KeyboardInterrupt:
        server.stop_server()
        print("Server stopped")
