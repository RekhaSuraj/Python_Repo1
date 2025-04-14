import sys

list1 = [10,20,30,40]

t1 = (10,20,30,40)

# sys.getsizeof() - fetches the memory size of the specified item in bytes
print(sys.getsizeof(list1)) # More memory usage
# 88

print(sys.getsizeof(t1)) # Less memory usage

# 72

# tuple supports only 2 methods
# index - returns the index position of the element specified
print(t1.index(40))
# 3

# count() - returns number of occurrences of a value
print(t1.count(20))
# 1

# Syntax Differences
# Feature	        List	                    Tuple
# Declaration	    my_list = [1, 2, 3]	        my_tuple = (1, 2, 3)
# Mutability	    Mutable (Changeable)	    Immutable (Unchangeable)
# Performance	    Slower (More Memory)	    Faster (Less Memory)
# Methods	More    (e.g., append(), remove())	Fewer (Only count(), index())
# Use Cases	        When data changes often	    When data remains fixed