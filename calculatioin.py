t=153
j=t
#5*4*3*2*1
p=0
c=[]
o=1
am=0
fac=[]
y=1
n=1
z=0
while t>0:
    c.append(t%10)
    t=t//10
    p+=1

    
for i in c:
    am=am+i**p
    o=o*i
for i in c:
    y=i
    for p in range (i-1,0,-1):
       y=y*p 
    fac.append(y)

while z<=j:
    z=z+n
    n=n+1
print(z)
print(sum(fac))
print (p)
print(sum(c))
print(o)
print(am)
l=0
for i in range (0,3+1):
    for i in range(i):
      print(l,end="")
      l+=1
    print()

a="sdj"
b="bsdsdj"
u=b[3:6]

for i in range(len(b)-len(a)+1):
   if b[i]==a[0]:
      
      if b[i:i+len(a)]==a:
         print ("its a sub sring at index",i,"to index",i+len(a))
      else:
          print("not a sub string till index",i)
      
a="asdsa"
c=""
t=len(a)-1
for i in range(t,-1,-1):
   c=c+a[i]
print(c)