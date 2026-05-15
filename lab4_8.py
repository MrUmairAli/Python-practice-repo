std=[
    { "name":"ali",
       "age":25,
       "marks":{ "english":85,"math":90,"science":78}
       },
    { "name":"bilal",
       "age":21,        
       "marks":{ "english":88,"math":79,"science":95}
       },
    {"name":"haroon",
       "age":22,   
       "marks":{"english":80,"math":74,"science":75}}  
    ]
c=input(" enter student name for data ").lower()
for i in std:
    if i["name"]==c:
        print(i)