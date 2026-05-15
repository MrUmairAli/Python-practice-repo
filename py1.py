n1=float(input("enter a no "))
o=""

while o != "=":
   o=str(input(" your operation:  "))
   if o=="=":
    break
   n2=float(input("enter an otheer no: "))
   if o=="+":
        n1=n1+n2
   elif o=="*":
        n1=n1*n2
   elif o=="/":
        n1=n1/n2
   elif o=="-":
        n1=n1-n2
   else:
      print(" invalid operator")
      
print("result is: " ,(n1))




