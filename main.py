import login
import menu
print("*"*10+"APPLO HOSPITAL"+"*"*10)
print("-"*40)
while True:
    print("*"*10+"Login Credentials"+"*"*10)
    user=input("Enter username = ").lower()
    pwd=input("Enter Password = ").lower()
    s=login.check(user,pwd)
    if s==1:
       menu.menu()
