c=input("enter a string ")
a=[]
d=[]
for i in c:
    if i not in d:
     a.append(c.count(i))
     d.append(i)
s=" "
for i in range(len(d)):
    s=s+str(a[i])+d[i]
print(s)