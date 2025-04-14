# List sort()

# sort() - arranges the list in ascending order by default, updates the original list itself
list1 = [40,3,12,9,23,67,44]
list1.sort()
# print(list1)
# [3, 9, 12, 23, 40, 44, 67]

# to print the elements of the list in descending order
list1.sort(reverse=True)
# print(list1)
# [67, 44, 40, 23, 12, 9, 3]

# sorted() - returns a new list containing all elements from the iterable in ascending order by default
list2 = [10,30,20,4,18,32]
list3 = sorted(list2)
print('list3',list3)
# list3 [4, 10, 18, 20, 30, 32]

print('list2',list2)
# list2 [10, 30, 20, 4, 18, 32]

# printing the list in reverse order for sorted()
list4 = sorted(list2,reverse=True)
print('list4 reverse=True',list4)
# list4 reverse=True [32, 30, 20, 18, 10, 4]


# Key Differences:
# Feature	                    sort()	            sorted()
#
# Modifies original list?	    ✅ Yes	            ❌ No
# Returns new list?	            ❌ No	            ✅ Yes
# Works with lists only?	    ✅ Yes	            ❌ No (works with any iterable)
# Memory efficient?	            ✅ Yes	            ❌ No (creates new object)

