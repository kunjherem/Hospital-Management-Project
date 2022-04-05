import mysql.connector as mq
def co():
    con=mq.connect(host="localhost",user='root',passwd="admin",database="hms")
    cu=con.cursor()
