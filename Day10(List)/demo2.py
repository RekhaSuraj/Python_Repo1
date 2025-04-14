# List indexing starts from 0 to n-1, each element will have a unique number - index
v1 = [10,20,30,40,50]

print('length of the list',len(v1))

# positive indexing
print('value at index 0:',v1[0])
print('value at index 1:',v1[1])
print('value at index 2:',v1[2])
print('value at index 3:',v1[3])
print('value at index 4:',v1[4])

# length of the list 5
# value at index 0: 10
# value at index 1: 20
# value at index 2: 30
# value at index 3: 40
# value at index 4: 50

# print('value at index 5:',v1[5])
# IndexError: list index out of range

# index() - Fetches the index position for the value specified
print('index of 30 is',v1.index(30))
# index of 30 is 2

print('index of 40 is',v1.index(40))
# index of 40 is 3

# -ve indexing
list2 = [5,10,15,20,'hi','hello']

print(list2[-1])
# hello

print(list2[-4])
# 15

# print(list2[-7])
# IndexError: list index out of range

print(list2.index('hi'))
# 4

# List allows duplicate values
# index usage without start index
l2 = [30,20,10,40,10]
print(l2.index(10))
# 2

# index usage with start index
print(l2.index(10,3))
# 4
