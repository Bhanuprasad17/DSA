def sumOfList(list1):
    if len(list1) == 0 :
        return 0
    if len(list1) == 1:
        return list1[0]
    return list1[0] + sumOfList(list1[1:])


print(sumOfList([1,2,3,4]))
print(sumOfList([]))