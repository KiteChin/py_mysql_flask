from pymysql import connect

class Mysql_Stu(object):
    def __init__(self):
        self.conn = connect(host = "localhost", port = 3306, user = 'root', password = 'qwe123456', database = 'Student', charset = 'utf8')
        self.csr = self.conn.cursor()

    def __del__(self):
        self.csr.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.csr.execute(sql)
        for temp in self.csr.fetchall():
            print(temp)

    def show_all_items(self):
        sql = "select * from stus;"
        self.execute_sql(sql)

    def show_cates(self):
        sql = "select Stu_ID from stus;"
        self.execute_sql(sql)

    def show_brands(self):
        sql = "select Stu_Name from stus;"
        self.execute_sql(sql)

    def add_brands(self):
        Stu_ID = input("pleas input the Student ID:")
        Stu_Name = input("pleas input the Student Name:")
        Stu_Class = input("pleas input the Student Class:")

        sql = """insert into stus values("%s","%s","%s",default,default)""" % (Stu_ID, Stu_Name, Stu_Class)
        self.csr.execute(sql)
        self.conn.commit()

    def run(self):
        while True:
            print("------jing_dong------")
            print("1 stand for all Student")
            print("2 stand for Student ID")
            print("3 stand for Student Name")
            print("4 add one Student information")
            num = input("Please input what you want qurey:")
            if num == "1":
                #all Student
                self.show_all_items()
            elif num == "2":
                #cates
                self.show_cates()
            elif num == "3":
                #brand cates
                self.show_brands()
            elif num == "4":
                self.add_brands()
            else:
                print("error,please try again")
    def ADD(self, P_ID, Stu_ID, Stu_Name, Stu_Class):
        sql = """insert into stus values("%s","%s","%s","%s",default,default)""" % (P_ID, Stu_ID, Stu_Name, Stu_Class)
        self.csr.execute(sql)
        self.conn.commit()

    def QUREY(self):
        sql = "select * from stus;"
        self.csr.execute(sql)
        return self.csr.fetchall()

    def DELETE(self, P_ID):
        sql = "delete from stus where P_ID=%s" %(P_ID)
        self.csr.execute(sql)
        self.conn.commit()

    def CHECK(self, P_ID, time):
        sql = "update stus set Check_St=1, Check_Time=%d where P_ID=%s" %(time, P_ID)
        self.csr.execute(sql)
        self.conn.commit()

    def INIT(self):
        sql = "update stus set Check_St=0, Check_Time=0"
        self.csr.execute(sql)
        self.conn.commit()



def main():
    # 1.creat a class for JD
    stu = Mysql_Stu()

    # 2. call the run function of class 
    stu.run()



if __name__ == "__main__":
    main()

