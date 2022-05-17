from flask import Flask,request
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from mysql_stu import *
import time
import chardet
from urllib.parse import unquote

app = Flask(__name__)
app.config['DEBUG'] = False
CORS(app, resources=r'/*')
CORS(app, supports_credentials=True)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

@app.route("/Stu/INIT")
def INIT():
    stu = Mysql_Stu()
    stu.INIT()
    return "INIT FINISH"

@app.route("/Stu/temp/<string:Stu_Name>")
def Detect(Stu_Name):
    temp = Stu_Name.encode("GB2312")    
    print(temp)

    return temp

@app.route("/Stu/ADD/<P_ID>/<Stu_Name>")
def ADD(P_ID,Stu_Name):
    if not is_number(P_ID):
        return "param error"

    stu = Mysql_Stu()
    stu.ADD(P_ID, Stu_Name)
    return "ADD FINISH"


@app.route("/Stu/QUERY")
def QUERY():
    stu = Mysql_Stu()
    sql_all = stu.QUERY()
    sql_all = str(sql_all)
    return sql_all

@app.route("/Stu/CHECK/<P_ID>/<Temperature>")
def CHECK(P_ID, Temperature):
    if not is_number(P_ID):
        return "param error"

    stu = Mysql_Stu()
    stu.CHECK(P_ID,Temperature,int(time.time()))
    return "CHECK"

@app.route("/Stu/DELETE/<P_ID>")
def DELETE(P_ID):
    if not is_number(P_ID):
        return "param error"
    stu = Mysql_Stu()
    stu.DELETE(P_ID)
    return "DELETE"

if __name__ == "__main__":
#    stu = Mysql_Stu()
    
    app.run(
            host='0.0.0.0',
            port=5000
    )
