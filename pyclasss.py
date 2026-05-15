a=[[1,2,3],[4,5,6],[7,8,9]]
b=[ x for i in a for x in i if x % 2==0]
print(b)
x={i:i*i for i in range (0,10)}
for p in range(0,10):
    if x[p]%2==0:
       del(x[p]) 
print (x)
i=True
u={"eyes":True
   ,"face":"pretty",
       "feelings":False}
if u["feelings"]==False:
    print(i)