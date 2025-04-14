# insert() - inserts the value specified at the specified index
li1 = ['blr','Mysore','Udupi','hospet', 'kollegal']
li1.insert(3,'Mandya')

print(li1)
# ['blr', 'Mysore', 'Udupi', 'Mandya', 'hospet', 'kollegal']

# li1.insert('TNPur')
# print(li1)
# TypeError: insert expected 2 arguments, got 1

# pop() - removes and returns the item at index value specified
# value_poped = li1.pop(2)
print('value poped',li1.pop(3))
# value poped Mandya
print('list after pop',li1)
# list after pop ['blr', 'Mysore', 'Udupi', 'hospet', 'kollegal']

# print('value removed is ',value_poped)
# value removed is  Udupi
print(li1)
# li1.pop(10)
# IndexError: pop index out of range


# remove() - removes first occurence of value
print(li1.remove('blr'))
print(li1)
# ['Mysore', 'Udupi', 'hospet', 'kollegal']
# ['Mysore', 'Mandya', 'hospet', 'kollegal']

# print(li1.remove('blr'))
# ValueError: list.remove(x): x not in list

