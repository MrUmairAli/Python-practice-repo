import random
choices=["cat","monkey","donkey","you"]
word=random.choice(choices)
live=6
guess=["","","","","","","","","","","","","","","","","","","",""]
a=["_" for i in range(len(word))]
my=True
for i in range(0,20):
 b=False
 print(a)   
 guess[i]=input("enter a letter  ")
 for j in range(len(word)):
   if guess[i]==word[j]:
       print ("corect")
       a[j]=guess[i]
       b=True
 if b==False:
   live=live-1
   print ("no match found try again")   
   print("lives left",live) 
     
 for n in range(len(word)):
  if a[n]=="":
      my=False  
 if live<=0 | my!=False:
      break      
m=""
for i in range(len(guess)):
      if guess[i]!="":
            m=m+guess[i]
print("you entersd ",m)
print ("corect was",word)
if word==m :
      print("you won with lives =",live)
else :
      print("you lost")
    
    