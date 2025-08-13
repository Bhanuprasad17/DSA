str1 = "bhanu".lower()
# print(str1[::-1])

str2 = ''

# for i in range(len(str1)-1,-1,-1):
#     str2 = str2 + str1[i]

# print(str2)

# print(len(str1)//2+1)
for i in range(len(str1)//2+1):
    str1[i],str1[len(str1)-1-i] = str1[len(str1)-1-i],str1[i] # worng because assignment not working with string they are immutable

print(str1)