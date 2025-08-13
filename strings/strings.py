# slicing systax str[start:stop:step]
# start: Index to begin from (inclusive)
# stop: Index to stop at (exclusive)
# step: Increment (+ for forward, - for backward)




str1 = "bhanu prasad"

# print(str1[::1])
# print(str1[::])
# print(str1[:6:2])
# print(str1[7:])
# print(str1[::])
# print(str1[::2])

# Example: string[:5] means "from the beginning to index 4"
# Example: string[5:] means "from index 5 to the end"
# Example: string[2:8] means "from index 2 to 7, step by 1"


text = "Python Programming"
print(text[2:10:2]) 
print(text[:10:2])  
print(text[2::2]) 
print(text[2:10])    
print(text[::2])     
print(text[:10])
print(text[2:])
print(text[:])     

print('----------------------------------')
print(text[:-1])
print(text[-len(text):-1])


# --------------------------------------------------------------------------------------------

str1 = "Bhanuprasad"

print(str1[0:len(str1):1])
print(str1[::1])
print(str1[::])

print(str1[:6:1])
print(str1[:6:2])
print(str1[::2])

print(str1[7::1])
print(str1[7::])
print(str1[::-1])
print(str1[:-11:-1])
print(str1[-11::-1]) # B



print(str1[-4::])
print(str1[-4:11:1])
print(str1[:-2])
print(str1[-5:-2])
print(str1[-1:-6:-1])