import pymysql
db = pymysql.connect("localhost", "root", "kuangjunhao29", "sp1")
cursor = db.cursor()
a = input("输入想要操作的表：P,S,SP。")
if(a == 'P'):
    PNO = input("输入PNO:")
    PNAME = input("输入PNAME:")
    WEIGHT = input("输入WEIGHT:")
    WEIGHT = float(WEIGHT)
    COLOR = input("输入COLOR:")
    CITY = input("输入CITY:")
    sql = "INSERT INTO P(PNO,PNAME,WEIGHT,COLOR,CITY) VALUES (\'%s\',\'%s\',%f,\'%s\',\'%s\')" % (PNO,PNAME,WEIGHT,COLOR,CITY)
if(a == "S"):
    SNO = input("输入SNO:")
    SNAME = input("输入SNAME:")
    CITY = input("输入CITY:")
    sql = "INSERT INTO S(SNO,SNAME,CITY) VALUES (\'%s\',\'%s\',\'%s\')" % (SNO,SNAME,CITY)
if(a =="SP"):
    SNO = input("输入SNO:")
    PNO = input("输入PNO:")
    QTY = input("输入QTY:")
    QTY = float(QTY)
    sql = "INSERT INTO SP(SNO,PNO,QTY) VALUES (\'%s\',\'%s\',%f)" % (SNO,PNO,QTY)
try:
    cursor.execute(sql)
    db.commit()
    print("SUCCEEDED.")
except:
    print("ERROR:FAILED TO INSERT.")
    db.rollback()
db.close()# w