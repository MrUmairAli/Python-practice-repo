import random
choices=["caat","moonkey","doonkey","yoou"]
word=random.choice(choices)
checking=[ i for i in word]
live=6
guess=["_"for i in word ]
choses=[]
b=True

while live>=0|b!=False:
 d=True
 e=True
 print(guess)
 c=input("enter your choice ")
 choses.append(c)
 for i in range(len(word)):
   if c==checking[i]:
     print(c," is in word at",i+1,"place")
     guess[i]=word[i]
     checking[i]=""
     d=False
     break
 if d==True:
   live=live-1
   print(c,"not found in word ")
 for i in range(len(guess)):
   if guess[i]=="_":
     e=False
 if e==True:
   b=False
     
if live<=0:
  print("you lost your lives ended")
  print("word was ",word)
else:
  print("you won !")
  print("you guessed corectly with", live ,"lives remaining ")  
  print("your guesses were ",choses)       
  print("word was ",word)