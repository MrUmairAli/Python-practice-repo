users=["admin","shopkeeper","librrary"]
passes=["1","2","3"]
c=input("enter your user name ")
b=input("entr your pass ")
l=None
for i in range(len(users)):
    if c==users[i]:
        if b==passes[i]:
            l=i+1
        else :
            print("wrong password")      
if l==1:
    print("welsome admin")
elif l==2:
     print("back to work amigoes")
elif l==3:
     print("what should we be doing today")
                
