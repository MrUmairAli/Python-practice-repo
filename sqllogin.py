import mysql.connector
d=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="log_history")
c=d.cursor()
def signin():
    n=input("enter username: ")
    p=input("enter password: ")
    c.execute("insert into records values(%s,%s)",(n,p))
    d.commit()
    print ("ADDED SUCESSFULLY")
def login():
    n=input("enter username: ")
    p=input("enter password: ")
    c.execute("SELECT * FROM records WHERE username=%s AND password=%s", (n, p))
    if c.fetchone():
        print("LOGIN SUCESSFULLY")
    else:
        print("invalid input")
while True:
    print("1.login")
    print("2.sigin")
    l=int(input("choice: "))
    if l==1:
        login()
    elif l==2:
        signin()
        
    else:
        print("invalid choice")
