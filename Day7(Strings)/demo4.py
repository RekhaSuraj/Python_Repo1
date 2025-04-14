# Slicing - is used to fetch a part (slice) of a string
# Syntax : [start:stop:step]
# start : The index from where you want to fetch the string, default start value is 0
# stop : Till where you want to fetch, default value is n, value +1 should be given 
# step : Jumps, default step value is 1

s1 = 'Python is a high level programming language'

# Positive Slicing
# Fetch high from the above string 
print(s1[12:16:1])
# high

# program
print(s1[23:30])


# Python, without start value - defaultly starts from 0
print(s1[:6])

# without stop value, defaultly returns till the length of the string
print(s1[12:])
# high level programming language

# Step value - jumps 2 positions and gives result
print(s1[::2])
# Pto sahg ee rgamn agae

# Fetch level 
print(s1[17:22])