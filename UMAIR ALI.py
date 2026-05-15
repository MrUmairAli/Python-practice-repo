# A
students = { "ammarah":{"age": 18,"marks":[90, 85, 88,78]},
             "sara":{"age": 19,"marks":[92, 81, 79,95]},
             "omar":{"age": 17,"marks":[70, 60, 65,45]}}
c={}

for i in students:
    total_marks = sum(students[i]["marks"])
    average_marks = total_marks / len(students[i]["marks"])
    c[i]=average_marks

print(c)
print(len(c))
t=students.keys()
print(list(t))
i=0
print(c)
for x in t:
    if c[x]<70:
        del(c[x])
    i=i+1
print(c)
p=c.values()
for i in p:
    t=i
    for x in p:
        if x>t:
            t=x
print(t)
print(c)
for i in c:
    if c[i]==t:
        print(i)


    
print(c)
p="pythonprograminglanguage"
t=len(p)//2
c=p[0:t]
v=p[t:len(p)]

v=v[::-1]

print(c+v)
print(v)