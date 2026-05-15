a=[]
x=int(input("enter no of words to add "))
for x in range (0,x):
    c=input("enter your word ")
    a.append(c)
print(a)

ct=("a","e","i","o","u")
R=[]
for x in a :
    total=0
    for t in x:
        if t in ct:
            total=total+1
    R.append(total)
mv={"":""}
for i in range(len(a)):
    mv.update({a[i]:R[i]})
del(mv[""])
print("total no of vowel is :",mv)