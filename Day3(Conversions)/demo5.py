# Conversion from decimal to hexadecimal, prefixed with 0x
# Contains values 0 - 9 and A-F/a-f
# Syntax : hex(num) - inbuilt method which converts from decimal to hex number

# Conversion from decimal to hex
a1 = 45
a2 = hex(a1)
print('hex value for a1',a2)
# hex value for a1 0x2d

print(hex(58))
# 0x3a

# Conversion from hex to decimal
h1 = 0x1234
print('decimal value for h1',h1)
# decimal value for h1 4660