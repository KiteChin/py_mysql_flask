from flask import Flask,request
from mysql_stu import *
import time

app = Flask(__name__)

@app.route("/Stu/INIT")
def INIT():
    stu.INIT()
    return "INIT FINISH"

@app.route("/Stu/ADD/<P_ID>/<Stu_Name>")
def ADD(P_ID,Stu_Name):
    print(P_ID)
    print(Stu_Name)
    stu.ADD(P_ID, Stu_Name)
    return "ADD FINISH"

@app.route("/Stu/QUERY")
def QUERY():
    sql_all = stu.QUERY()
    sql_all = str(sql_all)
    print(type(sql_all[0]))
    return sql_all

@app.route("/Stu/CHECK/<P_ID>/<Temperature>")
def CHECK(P_ID, Temperature):
    print(P_ID)
    print(Temperature)
    stu.CHECK(P_ID,Temperature, int(time.time()))
    return "CHECK"

@app.route("/Stu/DELETE/<P_ID>")
def DELETE(P_ID):
    print(P_ID)
    stu.DELETE(P_ID)
    return "DELETE"

if __name__ == "__main__":
    stu = Mysql_Stu()
    app.run()
