import pymysql
db = pymysql.connect("localhost", "root", "kuangjunhao29", "sp1")
cursor = db.cursor()
a = input("WHICH TABLE DO YOU WANT TO OPERATE:P,S,SP:")
if(a == 'S'):
    b = input("WHICH ROW DO YOU WANT TO UPDATE:SNO,SNMAE,CITY:")
    if(b == "SNO"):
        c = input("LOCATE:SNAME,CITY")
        if(c == "SNAME"):
            SNAME = input("INPUT SNAME:")
            SNO = input("WHAT SNO DO YOU WANT TO MODIFY:")
            sql = ("UPDATE S SET SNO = \'%s\' WHERE SNAME = \'%s\'") % (SNO,SNAME)

# if(a == 'P'):
# if(a == 'SP'):
try:
    cursor.execute(sql)
    db.commit()
    print("SUCCEEDED.")
except:
    db.rollback()
    print("FAILED.")