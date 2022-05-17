import socket
import time

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9000))
print(sock.recv(1024).decode())
while True:
    inf = input("what you want enter:")
    sock.sendall(inf.encode())
    if(inf == "ADD"):
        P_ID = input("P_ID:")
        sock.sendall(P_ID.encode())
        Stu_ID = input("Stu_ID:")
        sock.sendall(Stu_ID.encode())
        Stu_Name = input("Stu_Name:")
        sock.sendall(Stu_Name.encode())
        Stu_Class = input("Stu_Class:")
        sock.sendall(Stu_Class.encode())
    elif(inf == "QUREY"):
        temp = sock.recv(1024).decode()
        print(temp)
    elif(inf == "CHECK"):
        Stu_ID = input("P_ID:")
        sock.sendall(Stu_ID.encode())
    if(inf == "CLOSE"):
        break

# Finalizar a conexao
sock.close()
