import pymysql
db = pymysql.connect("localhost", "root", "kuangjunhao29", "sp1")
cursor = db.cursor()
sql = "SELECT * FROM P"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print("PNO  PNAME  WEIGHT  COLOR  CITY")
    for row in results:
        PNO = row[0]
        PNAME = row[1]
        WEIGHT = row[2]
        COLOR = row[3]
        CITY = row[4]
        print("%s   %s   %s    %s   %s" % (PNO, PNAME, WEIGHT, COLOR, CITY))
except: print("ERROR:failed to fetch data.")
db.close()