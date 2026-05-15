class hashing :
    h_list=[None]*8
    @staticmethod
    def check_size(h_list):
        a=0
        for i in h_list:
            if i is not None:
                a=a+1
        if a>=(len(h_list))*(2/3):
            t =len(h_list)
            for i in range(t):
                h_list.append(None)
    @staticmethod
    def hashing_l_t_s(data):
        for i in data:
            hashing.check_size(hashing.h_list)
            if isinstance(i, int):
                b=hashing.hashing_int(i)
                while hashing.h_list[b] is not None:
                    b=(b+1)%len(hashing.h_list)
                hashing.h_list[b]=i
            if isinstance(i,str):
                b=hashing.hashing_str(i)
                while hashing.h_list[b] is not None:
                    b=(b+1)%len(hashing.h_list)
                hashing.h_list[b]=i
            if isinstance(i,list) or isinstance( i, tuple) or isinstance(i, set):
                hashing.hashing_l_t_s(i)
    @staticmethod
    def hashing_int(data):
        hashing.check_size(hashing.h_list)
        bucket_no=data%len(hashing.h_list)
        return bucket_no
    @staticmethod
    def hashing_str(data):
        hashing.check_size(hashing.h_list)
        a=0
        for i in data:
            a=a+ord(i)
        bucket_no=a%len(hashing.h_list)
        return bucket_no
obj=hashing()
while True:
    print("1.int")
    print("2.string")
    print("3.list")
    print("4.set")
    print("5.tupple")
    print("6.float")
    print("7.exit")
    print("8.check hashed list")
    c=int(input("choose data type to hash : "))
    if c==1:
        a=int(input("enter your no: "))
        x=obj.hashing_int(a)
        while obj.h_list[x] is not None:
            x=(x+1)%len(obj.h_list)
        obj.h_list[x]=a
        print("hashing sucessful")
        print(obj.h_list)
    elif c==2:
        a=str(input("enter your string: "))
        x=obj.hashing_str(a)
        while obj.h_list[x] is not None:
            x=(x+1)%len(obj.h_list)
        obj.h_list[x]=a
        print("hashing sucessful")
        print(obj.h_list)
    elif c==3:
        a=int(input("enter no inputs for list: "))
        lis=[]
        for y in range(a):
            x=input(f"enter your {y}choice: ")
            lis.append(x)
        obj.hashing_l_t_s(lis)
        print("hashing sucessful")  
        print(obj.h_list)
    elif c==4:
        a=int(input("enter no inputs for sets: "))
        lis=set()
        for y in range(a):
            x=input(f"enter your {y}choice: ")
            lis.add(x)
        obj.hashing_l_t_s(lis)
        print("hashing sucessful")  
        print(obj.h_list)
    elif c==5:
        a=int(input("enter no inputs for tuple: "))
        lis=[]
        for y in range(a):
            x=input(f"enter your {y}choice: ")
            lis.append(x)
        lis=tuple(lis)
        obj.hashing_l_t_s(lis)
        print("hashing sucessful")  
        print(obj.h_list)
    elif c==6:
        a=float(input("enter your no : "))
        a=str(a)
        x=obj.hashing_str(a)
        while obj.h_list[x] is not None:
            x=(x+1)%len(obj.h_list)
        obj.h_list[x]=a
        print("hashing sucessful")
        print(obj.h_list)
    elif c==7:
        break
    elif c==8:
        print(obj.h_list)
    else:
        print("invalid choice")
    
    


    



