clas_math={
    "names":["alice","bob","charlie","david"],#addin    g students name sages using nested dict
    "ages":{"alice":20,"bob":21,"charlie":19,"david":22},
    "total marks":{"alice":75,"bob":86,"charlie":87,"david":92}     
    }
print("students with total marks greater than 80 are :")

for a in clas_math["total marks"]:
    if clas_math["total marks"][a]>80:
        print(a)
