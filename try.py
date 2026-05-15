a="5+3*2-8%4"
b=[i for i in a]
for i in range(len(b)):
    if b[i].isdigit():
        b[i]=float(b[i])
c=["%","/","*","+","-"]

# for i in c:
#    t=0
#    while t<len(b):
#      if b[t]==i:
#         if i=="%":
#             total=b[t-1]%b[t+1]
#             b[t-1]=total
#             del(b[t])
#             del(b[t+1])
#             t=-1
#      t=t+1
# print(b)
for i in c:
    t=0
    while t<len(b):
        if b[t]==i:
            if i=="%":
                b[t-1]=b[t-1]%b[t+1]
                
                del(b[t])
                del(b[t])
                print(b)
            elif i=="/":
                b[t-1]=b[t-1]/b[t+1]
                
                del(b[t])
                del(b[t])
                print(b)
            elif i=="*":
                b[t-1]=b[t-1]*b[t+1]
                
                del(b[t])
                del(b[t])
                print(b)
            elif i=="-":
                b[t-1]=b[t-1]-b[t+1]
                
                del(b[t])
                del(b[t])
                print(b)
            elif i=="+":
                b[t-1]=b[t-1]+b[t+1]
                
                del(b[t])
                del(b[t])
                print(b)


        t=t+1
