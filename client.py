import socket

s = socket.socket()
s.connect(('127.0.0.1', 64647))
while True:
    str = input("run command")
    s.send(str.encode())
    if(str == "Bye" or str == "bye"):
        break
    print("resp:", s.recv(1024).decode())
s.close()