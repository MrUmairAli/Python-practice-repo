a=[{"a":3},{"a":3}, {"a":34,"ab":7},{"a":34,"ab":7,}]

for i in range(len(a)):
    for t in range(len(a)):
        if i==t:
            continue
        else:
          if a[i]==a[t]:
             a[t]={"":""}
b=[]
for i in range(len(a)):
  if a[i]!={"":""}:
   b.append(a[i])
a=b
print (a)
