v1 = ['a','b','c',[[11,22,33,44],5,6,7,[10,20,30],'d','e'],20,40,[12,13,14,[1,2,3]],21]


print('index of 0:',v1[0])
print('index of 1:',v1[1])
print('index of 2:',v1[2])
print('index of 3:',v1[3])
print('index of 4:',v1[4])
print('index of 5:',v1[5])

print('index of 6:',v1[6])
print('index of 7:',v1[7])


# print 44
# print(v1[3][0][3])
# 44

# print 2
print(v1[6][3][1])
# 2

# slicing - positive slicing [1,2,3]
print(v1[6][3:])
# [[1, 2, 3]]

# -ve slicing [1,2,3]
print(v1[-2][-1:])
# [[1, 2, 3]]


# assignment
l2 = [1,2,['a',2,[3],5,6],[3,'d','r','t','d',[[11,22,33],[12,13,14],[34,56,78],11,12,13],'abc'],'python','java']

# print 12

# print 22