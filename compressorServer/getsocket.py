import socket
import threading
import json
import combination


def broadcast(data, client_socket):

    try:
        pkt = json.loads(data)
        if pkt:
            print("Received data:", data)
            print("Packet ID:", pkt['pid'])
            sc_pkt = '{"pid":0}'
            if pkt['pid'] == 10:  # 10부터 19까지는 meta cps 가 사용할 예정입니다. 
                flowrate = pkt['flowRate']
                pressure = pkt['pressure']
                sc_pkt = combination.optimalOp(30, flowrate) 
                str_pkt = json.dumps(sc_pkt.__dict__)
            if pkt['pid'] == 4:  # asking for status
                sc_pkt = '{"pid":1, "status" 0}'
                str_pkt = json.dumps(sc_pkt)
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


def start_threads(client_socket):
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            print(f"Conn dead")
            break  # 클라이언트가 연결을 종료하면 루프 종료
        print("Data received:", data)
        if (json.loads(data)['pid']):
            broadcast(data, client_socket)
    
def handle_client2(client_socket):
    data = client_socket.recv(1024)
    if not data:
        print(f"Conn dead")
    print("Data received:", data)
    if (json.loads(data)['pid']):
        broadcast(data, client_socket)
        client_socket.shutdown(socket.SHUT_RDWR)
        #client_socket.close()
        print("Socket closed after processing.")

    



def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 포트 재사용 설정
    server_socket.bind(('localhost', 7777))
    server_socket.listen(10)
    print("Server listening on port 7777...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established.")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()




start_server()