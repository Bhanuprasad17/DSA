arr = [5, 3, 8, 4, 2]

n = len(arr)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:       
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
print(arr)         
# Bubble Sort implementation


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
                
    return arr        
    
print(bubbleSort([5, 3, 8, 4, 2]))     
print(bubbleSort([1,2,3,4,5]))