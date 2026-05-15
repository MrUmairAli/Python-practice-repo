




clas_math={
    "names":["alice","bob","charlie","david"],#addin    g students name sages using nested dict
    "ages":{"alice":20,"bob":21,"charlie":19,"david":22},
    "math_marks":{"alice":85,"bob":92,"charlie":78,"david":90},
     "science_marks":{"alice":88,"bob":79,"charlie":95,"david":80},
     "computer_marks":{"alice":90,"bob":85,"charlie":88,"david":92}
    }
a= input("enter student name ")
print("student details are :")
print("stunde name :",a)
print("age :",clas_math["ages"][a])
print("math marks :",clas_math["math_marks"][a])
print("science marks :",clas_math["science_marks"][a])  
print("computer marks :",clas_math["computer_marks"][a])    
print(a)
