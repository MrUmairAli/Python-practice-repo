c=input(" enter a string :")
d=input(" enter a string :")
e=""
t=None
if c>d:
    for i in range (len(d)):
        e=e+c[i]+d[i]
        t=True
elif d>c:
    for i in range (len(c)):
        e=e+c[i]+d[i]
        t=False
else:
    for i in range (len(c)):
        e=e+c[i]+d[i]
if t==True:
    e=e+c[len(d):]
if t==False:
    e=e+d[len(d):]
print(e)
# q="sbcdg"
# v="sbcdgffte"
# x="sbcdgf"
# for i in v:
#     if i in q and i in x:
#         continue
#     else :
#         break
# print(i)

