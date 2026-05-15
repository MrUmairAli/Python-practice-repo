questions=["how many provinces of pakistan ", "how many colors are in a rainbow"," who is quaid"]
anwsers=[ "a.3 b.5 c.6 d.4","a.7 b.5 c.6 d.4","a.founder b.jailer c.portmanb d.techer"]
ca=["d","a","a"]
p=100
i=0
print (" welocme kbc")
print("whith every anwser your prize will be multiplied by 10")
w=input("enter any thing to start ")
while i <3:
    print(questions[i])
    print(anwsers[i])
    ua=input(" enter your anwser  " )
   
    if ua==ca[i]:
        print("correct anwser")
        p=p*10
    elif( (ua=="a"or ua=="b"or ua=="c"or ua=="c")and ua!=ca[i]):
         print ("wrong anwser -500")
         p=p-500
    else:
     print ("invalid choice")
    i=i+1
    
          
         
print(" game ended ")
print("you won" ,p)
    