text = 'dell'
dict = {}

for i in text:
    if i in dict:
        dict[i] = dict[i] + 1
    else :
        dict[i] = 1
        
        
for key,value in dict.items() :
    if value == 1 :
        print(key, ":", value)

print(dict)        
        