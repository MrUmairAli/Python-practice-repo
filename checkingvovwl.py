p="python is an amaxing programin language "
x=len(p)
print(x)
total=0
s=0
print(type(s))


while s<x-1:
    t=s+1
    
    if (p[s]==" "):
        if (p[t]=="a" )or (p[t]=="i" )or (p[t]=="e" )or (p[t]=="o") or (p[t]=="u"):
            total=total+1
    s=s+1       
print(total)
words=p.split()
t=0
print(words)
for i in words:
    if i[0] in "aeiou":
        t=t+1
print(t)