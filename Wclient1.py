import socket
while(True):
    s=socket.socket()
    s.connect(('localhost',5555))
    msg=input("You>>:")
    s.send(msg.encode())
    res=s.recv(1024).decode()
    print("Client>>:",res)

