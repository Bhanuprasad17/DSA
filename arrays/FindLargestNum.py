

arr = [3, 1, 4, 1, 5, 9]

def largestNum(arr):
    if not arr:
        return None
    largest_Num = float('-inf')
    for i in arr:
        if largest_Num < i :
            largest_Num = i
    return largest_Num       

print(largestNum(arr))
print(largestNum([9, 9, 9]))