# Nested List - A list inside another list (sub list)

l1 = [1,2,3,4,[11,12,13],[5,6,7],'a','b','c',[22,33,44],66]


print('length of the list:',len(l1))

print('hello')
print('index of 0:',l1[0])
print('index of 1:',l1[1])
print('index of 2:',l1[2])
print('index of 3:',l1[3])
print('index of 4:',l1[4])
print('index of 5:',l1[5])
print('index of 6:',l1[6])
print('index of 7:',l1[7])
print('index of 8:',l1[8])
print('index of 9:',l1[9])
print('index of 10:',l1[10])

# length of the list: 11
# index of 0: 1
# index of 1: 2
# index of 2: 3
# index of 3: 4
# index of 4: [11, 12, 13]
# index of 5: [5, 6, 7]
# index of 6: a
# index of 7: b
# index of 8: c
# index of 9: [22, 33, 44]
# index of 10: 66


# print('index of 11',l1[11])
# IndexError: list index out of range

# print 7 from the above list
print(l1[5][2])
# 7

print(l1[9][1])
# 33