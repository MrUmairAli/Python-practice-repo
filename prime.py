for num in range (2,102):
    is_prime= True
    for i in range (2,num):
     if num%i==0:
         is_prime= False
         break
    if is_prime:
        print (num,"is prime")
         
     # dic in dic     
library = {
    "History": {
        "titles": ["World War II", "Ancient Civilizations", "Cold War"],
        "available": {"World War II": True, "Ancient Civilizations": False, "Cold War": True}
    },
    "Technolo": {
        "titles": ["AI Revolution", "The Code Book", "Future Tech"],
        "available": {"AI Revolution": True, "The Code Book": True, "Future Tech": False}
    }
}
wars=[ x for y in library.values() for x , true in y["available"].items() if true ]
print(wars)