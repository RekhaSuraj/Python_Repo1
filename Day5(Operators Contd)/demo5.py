# Identity operator - Applicable for iterables (String, List, Tuple, Set, Frozen set, dictionary)
# There are 2 types - is , is not

list1 = [10,20,30]
list2 = [10,20,30]

# is - checks if both refer to the same object in memory(both have the same address/id), if yes it returns True
print(list1 is list2)

# id() - inbuilt method which returns the address (id) of the object
print('list1 address',id(list1))
# 3123543658880

print('list2 address',id(list2))
# 1825113888960

list3 = list1
print(list1 is list3)
# True
print('list3 address',id(list3))

# is not
print(list1 is not list2)
# True

print(list1 is not list3)
# False



