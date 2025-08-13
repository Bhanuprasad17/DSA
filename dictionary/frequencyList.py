list1 = [0,0,1,1,2,2,2]
# print(list1)
dict = {}

for i in list1:
    # print(i)
    if i in dict:
        dict[i] = dict[i] + 1
    else :
        dict[i] = 1

print(dict)        