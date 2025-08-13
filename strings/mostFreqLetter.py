str1 = 'astronomer'.lower()
str2 = 'moon starer'.lower()

str1_dict = {}
str2_dict = {}

for i in str1:
    if i == ' ':
        continue
    elif i in str1_dict :
        str1_dict[i] = str1_dict[i] + 1
    else :
        str1_dict[i] = 1
        
print(str1_dict)        


for j in str2:
    if j == ' ':
        continue
    elif j in str2_dict :
        str2_dict[j] = str2_dict[j] + 1
    else :
        str2_dict[j] = 1

print(str2_dict)        


if str1_dict == str2_dict :
    print('Anagram')
else :
    print('it is not anagram')

# maxfreq = max(str1_dict.values())
# print(maxfreq)

maxfreq = float('-inf')
for key,value in str1_dict.items():
    if maxfreq < value :
        maxfreq = value
print(maxfreq)

arr = []
    
for key,value in str1_dict.items():
    if value == maxfreq:
        arr.append(key)
        
print(arr)        
    
    
    
    