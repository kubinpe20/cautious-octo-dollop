import socket
import threading
import time
from datetime import datetime

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205

serversocket.bind((host, port))
clients = []
threads = []
lock = threading.Lock()
log_lock = threading.Lock()

log_file = open("log.txt", "a")


def read(client, addr):
    while True:
        msg = ""
        try:
            msg = client.recv(1024).decode('ascii')
        except:
            with lock:
                clients.remove(client)
                return
        if msg:
            with log_lock:
                log_file.write(datetime.now().strftime("%H:%M:%S ") + addr[0] + " " + msg)
                log_file.flush()
            with lock:
                for o in clients:
                    try:
                        o.sendall(bytes(msg, 'ascii'))
                    except:
                        pass

#ss
while True:
    print(host)
    print("Server listening on port", port)
    serversocket.listen()
    clientsocket, addr = serversocket.accept()
    clientsocket.sendall(b'Tent Man')
    x = threading.Thread(target=read, args=(clientsocket, addr,))
    threads.append(x)
    clients.append(clientsocket)
    x.start()
    print(addr)
clientsocket.close()
