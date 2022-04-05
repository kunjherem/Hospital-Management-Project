import mysql.connector as mq
def cnt(): #Function for my sql connection
    global con 
    global cu
    con=mq.connect(host="localhost",user='root',passwd="admin",database="hms") #Connecting to Sql
    cu=con.cursor()
###################################################################################################################################################
def viewpdata():
    cnt()
    s="select * from patient;"
    cu.execute(s)
    m=cu.fetchall()
    print("-"*60)
    print("p_id \t P_Name \t P_Age \t\t P_Gender \t p_contact_no \t P_Disease \t P_Status \t Consultant_Doc")
    try:
        for i in range(len(m)):
             print(str(m[i][0])+" \t "+m[i][1]+" \t\t "+str(m[i][2])+" \t\t "+m[i][3]+" \t\t "+str(m[i][4])+\
                   " \t "+m[i][5]+" \t " +m[i][6]+" \t\t "+m[i][7])
    except:
        print("Success")
###################################################################################################################################################
def remove():
    cnt()
    viewpdata()
    rpid=int(input("Select PID from above output to remove it : "))
    s="delete from patient where p_id="+str(rpid)+";"
    cu.execute(s)
    con.commit()
    print("Deleted Successfully")
    con.close()
###################################################################################################################################################
def doc():
    cnt()
    s="select * from doctor;"
    cu.execute(s)
    mm=cu.fetchall()
    print("-"*60)
    print("DID \t Doctor_Name \t\t Speciality \t Days Available")
    try:
        for i in range(len(mm)):
            print(mm[i][0]+" \t "+mm[i][1]+" \t "+mm[i][2]+" \t "+mm[i][3])
    except:
        print("Success")
###################################################################################################################################################
def patient():
    cnt()
    pn=input("Enter Patient Name: ").capitalize()
    pa=int(input("Enter Patient Age: "))
    pg=input("Enter Patient Gender: ").capitalize()
    pc=input("Enter Patient Contact Info: ")
    pd=input("Enter Patient Disease:  ").capitalize()
    print("Select Doctor from Below Table")
    doc()
    print("-"*60)
    pdoc=input("Enter Consultanting Doctor ID: ")
    ps=input("Patient wants to admitt? Yes or No : ").lower()
    if ps in ("yes"):
        S="insert into patient(P_Name,P_Age,P_Gender,P_Contact_NO,"\
           "P_Disease,P_Status,Consultant_Doc) values(%s,%s,%s,%s,%s,%s,%s)"
        cu.execute(S,(pn,pa,pg,pc,pd,ps,pdoc))
        con.commit()
        con.close()
        print("FORM FILLED SUCCESSFULLY")
    elif ps in ("no"):
        S="insert into patient(P_Name,P_Age,P_Gender,P_Contact_NO,P_Disease"\
           ",P_Status,Consultant_Doc) values(%s,%s,%s,%s,%s,%s,%s)"
        cu.execute(S,(pn,pa,pg,pc,pd,ps,pdoc))
        con.commit()
        con.close()
        print("FORM FILLED SUCCESSFULLY")
    else:
        print("Please Enter a Valid Input")
###################################################################################################################################################
def update():
    cnt()
    s="select * from patient;"
    cu.execute(s)
    m=cu.fetchall()
    print("-"*60)
    print("p_id \t P_Name")
    try:
        for i in range(len(m)):
             print(str(m[i][0])+" \t "+m[i][1])
    except:
        print("Success")
    upid=input("Select Patient ID from above: - ")
    print("1.)Patient Name\n2.)Patient Contact No.\n3.)Patient Age\n")
    uh=int(input("Select what you want to update from above: - "))
    if uh==1:
        upn=input("Enter Name :- ").capitalize()
        s="Update "+"Patient"+" set "+"P_Name"+"="+"'"+str(upn)+"'"+" where P_id="+str(upid)
        cu.execute(s)
        con.commit()
        print("Record Updated Successfully")
    elif uh==2:
        upn=input("Enter Contact No. :- ")
        s="Update "+"Patient"+" set "+"p_contact_no"+"="+"'"+str(upn)+"'"+" where P_id="+str(upid)
        cu.execute(s)
        con.commit()
        print("Record Updated Successfully")
    elif uh==3:
        upn=input("Enter Age :- ")
        s="Update "+"Patient"+" set "+"P_Age"+"="+"'"+str(upn)+"'"+" where P_id="+str(upid)
        cu.execute(s)
        con.commit()
        print("Record Updated Successfully")
    else:
        print("Enter a valid input: -")       
###################################################################################################################################################
def gbill():
     cnt()
     viewpdata()
     gpid=int(input("ENTER P_ID FROM ABOVE LIST: - "))
     nd=int(input("ENTER NO. OF DAYS ADMITTED: - "))
     cg=1000
     ta=nd*cg
     from datetime import datetime as k   #Importing for date and time
     o=k.now()
     bd=o.strftime("%Y-%m-%d")
     bt=o.strftime("%I:%m:%S")
     q="insert into bill(PID,ndays,charges,tamt,bdate,btime) values(%s,%s,%s,%s,%s,%s)"
     cu.execute(q,(gpid,nd,cg,ta,bd,bt))
     con.commit()
     q="select * from bill,patient where bill.pid=patient.p_id;"
     cu.execute(q)
     m=cu.fetchall()
     p="select * from patient where p_id="+str(gpid)
     cu.execute(p)
     m=cu.fetchall()
     print("-"*60)
     print("\t\tHOSPITAL MANAGEMENT SYSTEM")
     print("\n\nBill Date :-"+str(bd)+"\tBill Time :-"+str(bt))
     print("\nPatient Id :-"+str(gpid)+"\t\tPatient Name :-"+str(m[0][1]))
     print("\nPateint Age :-"+str(m[0][2])+"\tNo. of Days Admitted :-"+str(nd))
     print("\nCharge per day:-₹"+str(cg)+"\tTotal Amount :-₹"+str(ta))
     print("-"*60)
     pb=input("PRESS p TO PRINT BILL: - ").lower()
     if pb=="p":
         f=open("BILL.txt","w",encoding="utf-8")
         l0="\t\tHOSPITAL MANAGEMENT SYSTEM"
         l1="\n\nBill Date :-"+str(bd)+"\tBill Time :-"+str(bt)
         l2="\nPatient Id :-"+str(gpid)+"\t\t\tPatient Name :-"+str(m[0][1])
         l3="\nPateint Age :-"+str(m[0][2])+"\t\tNo. of Days admitted :-"+str(nd)
         l4="\nCharge :-₹"+str(cg)+"\t\tTotal Amount :-₹"+str(ta)
         l=[str(l0),str(l1),str(l2),str(l3),str(l4)]
         f.writelines(l)
         print("BILL GENERATED")
     else:
        print("Thanks for choosing us!")
###################################################################################################################################################
def viewbill(): 
    cnt()
    viewpdata()
    pid=input("Select P_Id from above for bill :- ")
    s="select * from bill where pid="+str(pid)
    cu.execute(s)
    m=cu.fetchall()
    print("-"*60)
    print("B_No. \t P_Id \t N_Days \t Charges \t Tamt \t Bdate \t\t BTime")
    print(str(m[0][0]) +"\t "+str(m[0][1]) +"\t "+str(m[0][2]) +"\t\t "+str(m[0][3]) +"\t\t "\
          +str(m[0][4]) +"\t "+str(m[0][5]) +"\t "+str(m[0][6]))
###################################################################################################################################################
def menu():
    x="y"
    while x=="y":
        print("1.)Available Doctors\n2.)Admission Form\n3.)Remove Patient\n4.)Update Info\n5.)Genertae Bill\n6.)View Bill\n7.)View Patient Table")
        ch=int(input("Select your choice from above options : "))
        if ch==1:
            doc()
        elif ch==2:
            patient()
        elif ch==3:
            remove()
        elif ch==4:
            update()
        elif ch==5:
            gbill()
        elif ch==6:
            viewbill()
        elif ch==7:
            viewpdata()
        x=input("Press y to continue : ")
    else:
        print("THANK YOU FOR USING OUR SOFTWARE")