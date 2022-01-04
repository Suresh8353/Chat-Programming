import socket
s=socket.socket()
s.bind(('localhost',5555))
s.listen(20)
print("Server ready to accept request from client side")
while(True):
    cs,ca=s.accept()
    cdata=cs.recv(1024).decode()
    print("Server>>:",cdata)
    ndata=input("\t\t\t\tYou>>:")
    cs.send(ndata.encode())
