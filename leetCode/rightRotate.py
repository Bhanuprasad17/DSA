arr = [1,2,3,4,5,6,7]
print(arr)
n = len(arr)-1
k = 1
k = k % n


# for i in range(0,k):
#     lastNum = arr[len(arr)-1]
#     for i in range(len(arr)-1,0,-1):
#         arr[i] = arr[i-1]
#     arr[0] = lastNum


for i in range(0,k):
    lastNum = arr[len(arr)-1]
    for i in range(len(arr)-1,-1,-1):
        arr[i] = arr[i-1]
    arr[0] = lastNum

print(arr)    
