str1 = 'google docs are better than word docs'

list1 = str1.split(' ')
print(list1)

max_length = float('-inf')

for i in list1:
    if len(i) > max_length :
        max_length = len(i)

print(max_length) 

output = []
for i in list1:
    if len(i) == max_length :
        output.append(i)

print(output)        