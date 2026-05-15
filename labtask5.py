#types of variable 
a= 5         #int
b="yr6"     #string
c=True       #bool

#operations and there uses
 #mathematical operations
a=a+a #same for (*,\,-)
b=b+b #used for concatination i strings other are not used
       # not used for bollean
 # comparison operator
c==a   # checking equality
c=a>a  #stores true\false by comparison
d="hsk" 
e=b>d # compare first digit if same then next and so on
      # no use for bolean
#assignment operators 
#(=,+=,-=,*=,\=,%=) usend to assing value to varible with or without any change
#logical operator 
#(and,or, not) used to connect multiple statements


#strings
# strigs is an itrable in python with many methods some are
a="wgehjhge"
e=a[5] # its is caled indexing it stores "h" in e as index starts from zero
# Sample string for examples
text = "  Hello World  "
word = "python"
sentence = "i love python programming"
num_str = "12345"
mix_str = "Python3"
print(text.upper())        # "  HELLO WORLD  "
print(text.lower())        # "  hello world  "
print(sentence.capitalize())  # "I love python programming"
print(sentence.title())       # "I Love Python Programming"
print("PyTHON".swapcase())    # "pYthon"
print(text.strip())     # "Hello World"
print(text.lstrip())    # "Hello World  "
print(text.rstrip())    # "  Hello World"
print(text.replace("World", "Python"))  # "  Hello Python  "
print(sentence.split())                # ['i', 'love', 'python', 'programming']
print(",".join(["a", "b", "c"]))       # "a,b,c"
print(sentence.find("python"))     # 7
print(sentence.rfind("o"))         # 12
print(sentence.index("love"))      # 2
print(sentence.count("o"))         # 3
print(sentence.startswith("i"))      # True
print(sentence.endswith("ing"))      # True
print("Hello".isalpha())    # True
print(num_str.isdigit())    # True
print(mix_str.isalnum())    # True
print("   ".isspace())      # True
print("hello".islower())    # True
print("HELLO".isupper())    # True
print("Hello World".istitle())  # True
print("Hello".center(10, '*'))   # "***Hello**"
print("Hi".ljust(6, '-'))        # "Hi----"
print("Hi".rjust(6, '-'))        # "----Hi"
print("5".zfill(4))              # "0005"
print("Hello".encode())           # b'Hello'
print("A\tB\tC".expandtabs(4))    # "A   B   C"
print(sentence.partition("python"))
# ('i love ', 'python', ' programming')

print(sentence.rpartition("python"))
# ('i love ', 'python', ' programming')
multi = "Line1\nLine2\nLine3"
print(multi.splitlines())   # ['Line1', 'Line2', 'Line3']
print("ß".casefold())       # "ss"  (more aggressive than lower)
name = "Ali"
age = 20
print("My name is {} and I am {} years old".format(name, age))
# "My name is Ali and I am 20 years old"

print("My name is {n} and I am {a}".format_map({'n': 'Ali', 'a': 20}))
# "My name is Ali and I am 20 years old"
trans = str.maketrans({"a": "@", "e": "3"})
print("apple".translate(trans))    # "@ppl3"UE5
# List Methods in Python - Examples

# 1. append()
fruits = ["apple", "banana"]
fruits.append("cherry")
print("append:", fruits)  # ['apple', 'banana', 'cherry']

# 2. extend()
fruits.extend(["mango", "grape"])
print("extend:", fruits)  # ['apple', 'banana', 'cherry', 'mango', 'grape']

# 3. insert()
fruits.insert(1, "orange")
print("insert:", fruits)  # ['apple', 'orange', 'banana', 'cherry', 'mango', 'grape']

# 4. remove()
fruits.remove("banana")
print("remove:", fruits)  # ['apple', 'orange', 'cherry', 'mango', 'grape']

# 5. pop()
removed_item = fruits.pop(2)
print("pop:", fruits, "| removed:", removed_item)  # ['apple', 'orange', 'mango', 'grape']

# 6. clear()
temp = fruits.copy()
temp.clear()
print("clear:", temp)  # []

# 7. index()
numbers = [10, 20, 30, 40, 30]
print("index:", numbers.index(30))  # 2

# 8. count()
print("count:", numbers.count(30))  # 2

# 9. sort()
numbers.sort()
print("sort ascending:", numbers)  # [10, 20, 30, 30, 40]
numbers.sort(reverse=True)
print("sort descending:", numbers)  # [40, 30, 30, 20, 10]

# 10. reverse()
letters = ['a', 'b', 'c']
letters.reverse()
print("reverse:", letters)  # ['c', 'b', 'a']

# 11. copy()
new_list = letters.copy()
print("copy:", new_list)  # ['c', 'b', 'a']

# 12. len()
print("len:", len(fruits))  # 4

# 13. max()
print("max:", max(numbers))  # 40

# 14. min()
print("min:", min(numbers))  # 10

# 15. sum()
print("sum:", sum(numbers))  # 130

# 16. list concatenation
a = [1, 2]
b = [3, 4]
print("concatenation:", a + b)  # [1, 2, 3, 4]

# 17. repetition
print("repetition:", a * 3)  # [1, 2, 1, 2, 1, 2]

# 18. membership test
print("membership:", 2 in a)  # True

# 19. list comprehension
squares = [x**2 for x in range(5)]
print("list comprehension:", squares)  # [0, 1, 4, 9, 16]

# 20. nested lists
matrix = [[1, 2], [3, 4]]
print("nested list:", matrix[1][0])  # 3
# ===============================
#       PYTHON SET METHODS
# ===============================

# Creating sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("A:", A)
print("B:", B)

# 1. add()
A.add(7)
print("add:", A)  # {1, 2, 3, 4, 7}

# 2. update()
A.update([8, 9])
print("update:", A)  # {1, 2, 3, 4, 7, 8, 9}

# 3. remove()
A.remove(9)
print("remove:", A)  # removes element 9

# 4. discard() – same as remove but doesn’t give error if not found
A.discard(10)
print("discard:", A)

# 5. pop()
popped = A.pop()
print("pop:", popped, "| set now:", A)

# 6. clear()
temp = A.copy()
temp.clear()
print("clear:", temp)  # empty set

# 7. copy()
C = B.copy()
print("copy:", C)

# 8. union()
print("union:", A.union(B))  # combines both sets

# 9. intersection()
print("intersection:", A.intersection(B))  # common elements

# 10. difference()
print("difference (A - B):", A.difference(B))

# 11. symmetric_difference()
print("symmetric_difference:", A.symmetric_difference(B))

# 12. issubset()
print("issubset:", {1, 2}.issubset(A))

# 13. issuperset()
print("issuperset:", A.issuperset({1, 2}))

# 14. isdisjoint()
print("isdisjoint:", A.isdisjoint({10, 11}))

# 15. intersection_update()
X = {1, 2, 3}
Y = {2, 3, 4}
X.intersection_update(Y)
print("intersection_update:", X)  # keeps only common elements

# 16. difference_update()
X = {1, 2, 3, 4}
Y = {3, 4}
X.difference_update(Y)
print("difference_update:", X)  # removes common elements

# 17. symmetric_difference_update()
X = {1, 2, 3}
Y = {3, 4, 5}
X.symmetric_difference_update(Y)
print("symmetric_difference_update:", X)  # keeps non-common

# Length of a set
print("len:", len(A))

# Membership test
print("membership:", 4 in A)

# ===============================
#       PYTHON TUPLE METHODS
# ===============================

# Creating a tuple
tup = (10, 20, 30, 20, 40)
print("\nTuple:", tup)

# 1. count()
print("count(20):", tup.count(20))  # 2

# 2. index()
print("index(30):", tup.index(30))  # 2

# Accessing elements
print("tup[1]:", tup[1])  # 20

# Slicing
print("tup[1:4]:", tup[1:4])  # (20, 30, 20)

# Concatenation
tup2 = (50, 60)
print("concatenation:", tup + tup2)

# Repetition
print("repetition:", tup * 2)

# Membership
print("membership (30 in tup):", 30 in tup)

# Iteration
for item in tup:
    print("tuple item:", item)

# Length
print("len:", len(tup))

# min and max
print("min:", min(tup))
print("max:", max(tup))

# sum
print("sum:", sum(tup))

# Nested tuple
nested = ((1, 2), (3, 4))
print("nested access:", nested[1][0])  # 3

# Tuple unpacking
a, b, c, d, e = tup
print("unpacked:", a, b, c, d, e)
# ===============================
#       PYTHON DICTIONARY METHODS
# ===============================

# Creating a dictionary
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}

print("Original dictionary:", student)

# 1. get()
print("get('name'):", student.get("name"))  # Ali
print("get('gender', 'Not Found'):", student.get("gender", "Not Found"))

# 2. keys()
print("keys:", student.keys())  # dict_keys(['name', 'age', 'grade'])

# 3. values()
print("values:", student.values())  # dict_values(['Ali', 20, 'A'])

# 4. items()
print("items:", student.items())  # dict_items([('name', 'Ali'), ('age', 20), ('grade', 'A')])

# 5. update()
student.update({"age": 21, "city": "Karachi"})
print("update:", student)  # {'name': 'Ali', 'age': 21, 'grade': 'A', 'city': 'Karachi'}

# 6. pop()
removed = student.pop("grade")
print("pop:", student, "| removed:", removed)

# 7. popitem()
key, value = student.popitem()
print("popitem:", key, "=", value)
print("After popitem:", student)

# 8. setdefault()
student.setdefault("gender", "Male")
print("setdefault (adds if missing):", student)

# 9. copy()
copy_dict = student.copy()
print("copy:", copy_dict)

# 10. clear()
temp = copy_dict.copy()
temp.clear()
print("clear:", temp)  # {}

# 11. fromkeys()
keys = ["id", "name", "marks"]
new_dict = dict.fromkeys(keys, 0)
print("fromkeys:", new_dict)  # {'id': 0, 'name': 0, 'marks': 0}

# 12. dict comprehension
squares = {x: x*x for x in range(5)}
print("dict comprehension:", squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 13. len()
print("len:", len(student))  # number of key-value pairs

# 14. Membership test
print("'age' in student:", "age" in student)
print("'grade' not in student:", "grade" not in student)

# 15. Looping through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"{key} → {value}")

# 16. Nested Dictionary
school = {
    "student1": {"name": "Ali", "marks": 85},
    "student2": {"name": "Sara", "marks": 90}
}
print("\nNested dict:", school)
print("Access nested:", school["student2"]["marks"])  # 90