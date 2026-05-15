library={
    "fiction":{
        "titles":["1984","the hobbit","1984"],
    "available":{"1984":True,"the hobbit":False,"duen":True,"duen":True}
    },
    "science":{
        "titles":["a brief history ","cosmos"],
      "available":{"a brief history ":True,"cosmos":False}        
      }
    }

a = [x for x in library["fiction"]["available"].items()]
print(a)


