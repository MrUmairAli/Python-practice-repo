import json
history={}
def afile(h):
    with open ("hist.json","w") as t:
        json.dump(h,t)
def rfile(h):
    global history
    try:
        with open("hist.json", "r") as t:
            history = json.load(t)    
        print("data collected")
    except:
        history = {}                  
        print("no data found")

    

    
def sign(name,pas):
    history[name]=pas
    print("added sucessully")
    afile(history)
def login(name ,pas):
    if name in history:
        if history[name]==pas:
            print("login sucessfully")
        else :
            print("inavlid pass")
    else:
        print("name not found")
rfile(history)
while True:
    print("1.login")
    print("2.sigin")
    c=int(input("choice: "))
    if c==1:
        n=input("enter username ")
        p=input("enter password ")
        login(n,p)
    elif c==2:
        n=input("enter username ")
        p=input("enter password ")
        sign(n,p)
        afile(history)   
    else:
        print("invalid choice")

