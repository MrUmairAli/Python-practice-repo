def error(exception):
    pass
try:
    a=int(input ("enter a no"))
except ValueError as e:
   e= print(error("try a no" ))
finally:
    print("done")