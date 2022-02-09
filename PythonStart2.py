from math import pi
print(pi)
a = 10
b = 10
print(id(a), id(b))
x = 6
print(type(x))
print(isinstance(x, int))
print(isinstance(x, str))
x = 'Hello'
x = 'X' + x[1:]
print(x)
x = [1, 2, 3, 4]
x[0] = 'Hello'
print(x)