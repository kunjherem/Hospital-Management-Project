import mysql.connector as mq
def check(u,p):
    con=mq.connect(host="localhost",user='root',passwd="admin",database="hms")
    cu=con.cursor()
    s="select * from login;"
    cu.execute(s)
    m=cu.fetchall()
    data=dict(m)
    #print(data)
    if u in data:
        if p==data[u]:
            print("LOGIN SUCCESSFULLY")
            print("-"*40)
            return 1
        else:
            print("Invaild Password")
    else:
        print("Invalid Username")
