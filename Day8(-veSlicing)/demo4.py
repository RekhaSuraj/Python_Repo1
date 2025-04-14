str2 = 'welcome To Python training'

# swapcase() - converts upper case to lower and lower case to upper
print(str2.swapcase())
# WELCOME tO pYTHON TRAINING

# casefold() - converts the string to lower case and is considered more aggressive and comprehensive comparec to lower()
# Deals with unicode characters as well
print(str2.casefold())

# index() - returns the lowest index of the substring specified
# without start and end index
print(str2.index('o'))
# 4

# with start index
print(str2.index('o',5))
# 9

# with start and end index
print(str2.index('o',5,15))
# 9

# print(str2.index('x'))
# ValueError: substring not found

# find() - Returns the index or position of the substring specified
print(str2.find('e'))
# 1

# Returns -1 if substring is not found
print(str2.find('x'))
# -1

# str2.startswith()
# str2.endswith()

# count - Returns the count of the substring specified
print('***'*10)
str2 = 'Welcome'
print(str2.count('o'))
# 1

# substring if not available, it returns 0
print(str2.count('s'))
# 0

print(str2.count('e'))
# 2

# isupper() - Checks if the string is in upper case, returns True if it is in upper case
str3 = 'monday is powerful'
print(str3.isupper())
# False

# islower() - Checks if the string is in lower case, returns True if it is in lower case
print(str3.islower())
# True


