from flask import Flask,request
from mysql_stu import *
import time

app = Flask(__name__)

@app.route("/Stu/INIT")
def INIT():
    stu.INIT()
    return "INIT FINISH"

@app.route("/Stu/ADD/<P_ID>/<Stu_ID>/<Stu_Name>/<Stu_Class>")
def ADD(P_ID,Stu_ID,Stu_Name,Stu_Class):
    print(P_ID)
    print(Stu_ID)
    print(Stu_Name)
    print(Stu_Class)
    stu.ADD(P_ID, Stu_ID, Stu_Name, Stu_Class)
    return "ADD FINISH"

@app.route("/Stu/QUREY")
def QUREY():
    print(sql_all)
    sql_all = stu.QUREY()
    sql_all = str(sql_all)
    return sql_all

@app.route("/Stu/CHECK/<P_ID>")
def CHECK(P_ID):
    print(P_ID)
    stu.CHECK(P_ID,int(time.time()))
    return "CHECK"

@app.route("/Stu/DELETE/<P_ID>")
def DELETE(P_ID):
    print(P_ID)
    stu.DELETE(P_ID)
    return "DELETE"

if __name__ == "__main__":
    stu = Mysql_Stu()
    app.run()
