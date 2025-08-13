
str1 = 'AJAY'.lower()
str2 = 'JAYA'.lower()

str1_dict = {}
str2_dict = {}


for i in str1:
    if i in str1_dict:
        str1_dict[i] = str1_dict[i] + 1
    else :
        str1_dict[i] = 1

for i in str2:
    if i in str2_dict:
        str2_dict[i] = str2_dict[i] + 1
    else :
        str2_dict[i] = 1

print(str1_dict)        
print(str2_dict)     

if str1_dict == str2_dict:
    print("Anagrams")
else:
    print("Not Anagrams")