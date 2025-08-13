
def largest_num(arr):
    
    largestNum = float('-inf')
    secondLargest = float('-inf')
    
    for i in range(len(arr)):
        if largestNum < arr[i] :
            secondLargest = largestNum 
            largestNum = arr[i]
        elif arr[i] != largestNum and arr[i] > secondLargest:
            secondLargest = arr[i]

    if secondLargest == float('-inf'):
        secondLargest = 'No Largest Number'        
            
    return [largestNum,secondLargest]
    
print(largest_num([3, 1, 4, 1, 5, 9]))    
print(largest_num([9,9, 9]))  

