import mysql.connector
cobj = mysql.connector.connect(host="localhost",username="root",password="@BroPro_07070.",database="schooldb")
cursor = cobj.cursor()

query = "select * from students;"
cursor.execute(query)
rows = cursor.fetchall()
for i in rows:
    print(i)