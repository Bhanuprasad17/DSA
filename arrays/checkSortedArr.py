


# def is_sorted(arr):
#     for i in range(1,len(arr)):
#         if arr[i] < arr[i- 1] :
#             return False
#     return True

# print(is_sorted([1, 2, 3, 4, 5]))   
# print(is_sorted([1, 3, 2, 4]))


def rotateArr(arr,k):

    n = len(arr)

    for j in range(k):
            lastNum = arr[n-1]
            for i in range(n-1,0,-1):
                arr[i] = arr[i-1]
            arr[0] = lastNum

    return arr

print(rotateArr([1,2,3,4,5],2))    
