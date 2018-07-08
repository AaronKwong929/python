import pymysql
db = pymysql.connect("localhost", "root", "kuangjunhao29", "sp1")
cursor = db.cursor()
a = input("WHICH TABLE DO YOU WANT TO OPERATE:P,S,SP:")
if(a == "S"):
    b = input("WHICH ROW DO YOU WANT TO OPERATE:SNO,SNAME,CITY")
    if(b == "SNO"):
        SNO = input("INPUT SNO:")
        sql = "DELETE FROM S WHERE SNO = \'%s\'" % (SNO)
    if(b == "SNAME"):
        SNAME = input("INPUT SNAME:")
        sql = "DELETE FROM S WHERE SNAME = \'%s\'" % (SNAME)
    if(b == "CITY"):
        CITY = input("INPUT CITY:")
        sql = "DELETE FROM S WHERE CITY = \'%s\'" % (CITY)
# if(a == "P"):
# if(a == "SP"):
try:
    cursor.execute(sql)
    db.commit()
    print("SUCCEEDED.")
except:
    print("ERROR:FAILED TO DELETE.")
    db.rollback()
db.close()