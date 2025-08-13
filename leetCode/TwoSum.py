list = [2,7,11,15,9]

target = 9
output = []

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] + list[j] == target :
            output.append([i,j])
    if list[i] == target:
        output.append([i])       


print(output)