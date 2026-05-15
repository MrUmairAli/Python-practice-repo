'''s="learning pythom is fun and powerfull"
words=s.split()
print(words)
l=0
for i in range(len(words)):
    if l%2!=0:
        words[i]=words[i][::-1]
    l=l+1
print(words)
s=""
for i in words:
    s=s+i+" "
print(s)
num=[1,2,3,3,4,5,6,7,6,7,7,8]
a=list(set(num))
p=4
p=list(p)'''
std=[ {'name':"umair","marks":[1,2,3,4]},
     {"name":"ahad","marks":[2,3,4,5,6,7]},
     {"name":"ali","marks":[00,9,8,7,6,]}]

for i in range(len(std)):
    avg = sum(std[i]["marks"])/len(std[i]["marks"])
    std[i].update({"avg":avg})
    
    print(avg)
print(std)
t=[]
mat=[[45,5,95],[20,10,2],[14,3,0]]
for i in mat:
    for x in range(len(i)):
        if x==0 or x==(len(i)-1):
           if i[x]%5==0:
              print(i[x],"is divisible by 5")
           else:
             print(i[x],"is not divisible by 5")
               
    '''
    c,*d,e=tuple(i)
    if c%5==0:
        print(c,"is divisible by 5")
    else:
        print(c,"is not divisible by 5")
    if e%5==0:
        print(e,"is divisible by 5")
    else:
        print(e,"is not divisible by 5")'''
    '''for x in range(len(i)):
        if x%2==0:
            if i[x]%5== 0:
                   print(i[x],"is divisible by 5")
            else:
                   print (i[x],"is not divisible by 5")'''
