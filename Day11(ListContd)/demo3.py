# slicing

list1 = [10,20,'welcome',30,40,'hi','hello','welcome']
# start:stop:step

# +ve slicing
# welcome, 30
print(list1[2:4])
# ['welcome', 30]

# -ve slicing
# 'hello','welcome']
print(list1[-2:])
# ['hello', 'welcome']

# printing list in reverse order using step -1
print(list1[::-1])
# ['welcome', 'hello', 'hi', 40, 30, 'welcome', 20, 10]



