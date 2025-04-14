# List Methods
l1 = [11,22,33,44]
# print(help(list))
l2 = [55,66,77]

# List concatenation using + operator
print(l1+l2)
# [11, 22, 33, 44, 55, 66, 77]

# append() - concatenates the specified value at the end of the list
l1.append(99)
print(l1)
# [11, 22, 33, 44, 99]


list1 = ['hi','hello','welcome']
list1.append('Python')
print(list1)
# ['hi', 'hello', 'welcome', 'Python']

# list1.append(l1)
# print(list1)
# ['hi', 'hello', 'welcome', 'Python', [11, 22, 33, 44, 99]]

# extend() - combines/appends 2 lists into a single list
list1.extend(l1)
print(list1)
# ['hi', 'hello', 'welcome', 'Python', 11, 22, 33, 44, 99]