#i=1
#while i<10:#
    #print (i * '*')
    #i=i+1
   # weight=int(input("weight= "))
#p=input(" kg or lb= ")
#if p=="kg":
   # print("weight in lb is "+str(weight/0.45))
#elif p=="lb":
    #print("weight in kg is "+str(weight*0.45))
#else:
 #print("fuck off invalid choice")
#for numbers in range(5,50,9):
   # print (numbers)

 
#a=[1,2,3,4,5,6,7,8,9]
#print (7 in a)
#a[4]=6
#print (a)
#phone=["+923119577027","+9231551350978"]
#pak=[p.split("+92")[1]for p in phone]
#i=0
#while i!=2:
 #print("03"+pak[i])
 #i=i+1
#u=["hamza",18,"ics","imcb","male"]
#name,age,*_,gender=u
#print (f'name {name}  age {age} gender  {gender}.')
#j="javascript"
#r=" web development"
#print (f'{j} is a very popular programing language us  for {r}.')

def rock():
 import random
 choics =["r","p","s"]
 player= input(" your choice 'r','p','s'  ").lower()

 if player not in choics:
  print("invalid choice")
  
 pc=random.choice(choics)
 if pc==player:
  print ("its a tie ")
 elif ( pc=="r"and player=="p")or\
      ( pc=="p"and player=="s")or\
      ( pc=="s"and player=="r"):
       print("you win")    
 else :
  print("you lost")  
 
 
rock() 