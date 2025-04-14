# -ve Slicing
# Starts from -1 to -n
# Syntax : iterable[start:stop:step]
s1 = 'Python is a Dynamically typed language'

# Fetch 'typed' from the above string using -ve slicing
print(s1[-14:-9])
# typed

# FEtch 'Dynamic' from the above string using -ve slicing
print(s1[-26:-19])
# Dynamic

# +ve slicing
print(s1[12:19])
# Dynamic

print(s1[-26:19])
# Dynamic

# Fetch depyt
print(s1[-10:-15])
# empty string

# Fetch nohtyP
print(s1[5:0])
# empty string

# NOTE : Start index should always be smaller than the Stop Index