#from collections import deque
#s=deque["ali","you","me","it","he"]
#x=[x*2 for x in range(0,10)]
#x.append(-5)
#c=[abs(x) for x in x]
#print(c)
#print(s.index(7,5,9))
#s.popleft()
#print(s)
#s.popleft()
#print(s)
#print(s)
#s.popleft()
#print(s)
a={x:x*2 for x in range(0,3)}
print(a.values())
print(a.keys())
print(a.items())
print(a.get(3,"unknown"))
a[4]="hello"
print(a.items())
print(list(a))
print(sorted(a))
print(1 in a)
print(10 in a)
print("hello" in a)
for i,u in  a.items():
  print(i,u)
for i,u in  enumerate (a.keys()):
    print(i,u)
for  x in reversed(range(1,10,2)):
    print(x)
#print(a[3])