import math

try:
    a=5/0
    print(a)
except ArithmeticError:
    print("Raise Arithmetic Exception")


try:
    a=[1, 2, 3]
    print(a[3])
except LookupError:
    print("Raise Index out of Bound")


try:
    a= {'a':1, 'b':2}
    print(a['c'])
except KeyError:
    print("Raise Key not Found")
