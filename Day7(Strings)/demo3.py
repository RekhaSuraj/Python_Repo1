# Negative Indexing - Index starts from -1 to n
# Moves from right to left, last index will be the length of the string(-)

s2 = 'Happiness is everything'

print(len(s2))
# 23

print('index value at -1:',s2[-1])
print('index value at -2:',s2[-2])
print('index value at -3:',s2[-3])
print('index value at -4:',s2[-4])
print('index value at -5:',s2[-5])
print('index value at -6:',s2[-6])
print('index value at -7:',s2[-7])
print('index value at -8:',s2[-8])
print('index value at -9:',s2[-9])

print('index value at -10:',s2[-10])
print('index value at -11:',s2[-11])
print('index value at -12:',s2[-12])
print('index value at -13:',s2[-13])
print('index value at -14:',s2[-14])
print('index value at -15:',s2[-15])
print('index value at -16:',s2[-16])
print('index value at -17:',s2[-17])
print('index value at -18:',s2[-18])
print('index value at -19:',s2[-19])

print('index value at -20:',s2[-20])
print('index value at -21:',s2[-21])
print('index value at -22:',s2[-22])
print('index value at -23:',s2[-23])

# print('index value at -24:',s2[-24])
# IndexError: string index out of range

str1 = 'Honesty is the best policy'

# Fetch e using -ve indexing
print(str1[-23])
print(str1[-10])

# +ve indexing
print(str1[3])