# If we donot specify any index number within pop(), it takes the default value as -1 (last index to the right)
list1 = ['Vittal','Rao','Kumar','Ram']
list1.pop()
print(list1)
# ['Vittal', 'Rao', 'Kumar']

# del list - deletes the entire list along with elements from the memory
# syntax : del list2
list2 = [11,22,33,44,55]
print(list2)
# ['Vittal', 'Rao', 'Kumar']
del list2

print(list2)
# NameError: name 'list2' is not defined. Did you mean: 'list1'?

