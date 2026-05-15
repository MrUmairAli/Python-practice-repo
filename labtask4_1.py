library={
    "fiction":{
        "titles":["1984","the hobbit","1984"],
    "available":{"1984":True,"the hobbit":False,"duen":True}
    },
    "science":{
        "titles":["a brief history ","cosmos"],
      "available":{"a brief history ":True,"cosmos":False}        
      }
    }
b=[ x for y in library.values() for x  , true in y["available"].items()if true]
print(b)
c=input("enter your new category ")
d=int(input ("no of books you want to add  "))
cd=[]
for i in range(0,d):
    p=input ("enter name of books ")
    cd.append(p)
    
print(cd)
print (c)
t=[]
for x in cd:
    print("for", x)
    l=(input( '''enter "t"if available else "F" ''').upper())
    if l=="T"or l=="t":
        t.append(True)
    elif l=="F"or l=="f":
        t.append(False)
    else:
        print("invalid input , setting default to False")
        t.append(False)
av = dict(zip(cd, t))
library[c]={"titles":cd,"available":av}
print(library)
tit=[x for y in library.values()for x in y["titles"]]
tit=set(tit)
print(tit)
