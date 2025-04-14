# Conversions
# int, float

# Implicit casting
var1 = 20
# print(type(var1))
# <class 'int'>

var2 = 35.5
# print(type(var2))
# <class 'float'>

var3 = var1+var2
# print(var3)
# 55.5
# print(type(var3))
# <class 'float'>


# Explicit casting
# conversion from int to float
v1 = 30
print('before typecasting:',type(v1))
# before typecasting: <class 'int'>
v2 = float(v1)
print(v2)
# 30.0
print('after tycasting:',type(v2))
# after tycasting: <class 'float'>

# conversion from float to int
a1 = 45.678
a2 = int(a1)
print(int(a2))
print(type(a2))
# <class 'int'>
# 45

b1 = "True"
print('Before conversion b1',type(b1))
# <class 'str'>

b2 = bool(b1)
print('After conversion b2',type(b2))

