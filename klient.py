import socket
import tkinter as tk
# import tkinter
import fileinput
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205

window = tk.Tk()
window.title("CHAT")
window.geometry("500x500")

s.connect((host, port))


def read(name):
    while True:
        msg = s.recv(1024).decode('ascii')
        if msg:
            print(msg)


x = threading.Thread(target=read, args=(1,))
x.start()

while True:
    for line in fileinput.input():
        s.sendall(bytes(line, 'ascii'))
s.close()
