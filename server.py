import socket
from mysql_stu import *
import time

HOST_1 = '127.0.0.1'
HOST = '0.0.0.0'
PORT = 9000

# establish the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = sock.bind((HOST,PORT))
sock.listen(1)

# establish the mysql for Student
stu = Mysql_Stu()

connection, address_client = sock.accept()
connection.sendall("OK".encode())
while True:
    client_data = connection.recv(30).decode()

    if(client_data == "ADD"):
        print("ADD start")
        P_ID = connection.recv(30).decode()
        Stu_ID = connection.recv(30).decode()
        Stu_Name = connection.recv(30).decode()
        Stu_Class = connection.recv(30).decode()
        stu.ADD(P_ID, Stu_ID, Stu_Name, Stu_Class)
        print("ADD completed")
    elif(client_data == "INIT"):
        print("INIT start")
        stu.INIT()
        print("INIT end")
    elif(client_data == "QUREY"):
        print("QUREY start")
        sql_all = stu.QUREY()
        sql_all = str(sql_all)
        connection.sendall(sql_all.encode())
        print("QUREY end")
    elif(client_data == "CHECK"):
        print("Check start")
        P_ID = connection.recv(30).decode()
        stu.CHECK(P_ID,int(time.time()))
        print("Check end")
    elif(client_data == "DEL"):
        print("DEL start")
        stu.DEL()
        print("DEL end")
    elif(client_data == "CLOSE"):
        break
connection.sendall("CLOSE!!".encode())
connection.close()

