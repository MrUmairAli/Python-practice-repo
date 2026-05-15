class humman():#one classs method can not talk with another method but object can
 color="red"
c=humman()
print(c.color)
t=humman()
t.color="pink"

print(t.color)
print(c.color)
print(len(dir(list)))
class atm():
   def __init__(self):
     self.pin=""
     self.balance=0
     self.menu()
   def menu(self):
    while True:
     print("1.create pin:")
     print("2.withdraw:")
     print("3.deposit:")
     print("4.checkbalance")
     c=int(input("enter your choice: "))
     if c==1:
       y=input("create pin: ")
       self.pin=y
     elif c==2:
       l=str(input("enter your pin: "))
       if self.pin==l:
         y=int(input("enter amout to withdraw: "))
         if y<= self.balance:
           self.balance=self.balance-y
           print(f"withdraw sucessfully amoutwithdraw{ y } remaining{ self.balance }")
         else:
           print(f"amount is more than balance, balance is :",self.balance)
       else:
         print("wrong passwod")
     elif c==3:
       a=int(input("enter amount yo add: "))
       self.balance=self.balance+a
       print("added sucessfully balance is",self.balance)
     elif c==4:
       l=str(input("enter your pin: "))
       if self.pin==l:
         print("balance is :",self.balance)
       else:
         print("invald pin")
       



o=atm()
