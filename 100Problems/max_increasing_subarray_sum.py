


def max_increasing_subarray_sum(arr):
    max_sum = current_sum = arr[0]

    for i in range(1,len(arr)):

        if arr[i] > arr[i-1]:
            current_sum = current_sum + arr[i]
        else :
            current_sum = arr[i]    
        max_sum = max(max_sum,current_sum)
    return max_sum                 

print(max_increasing_subarray_sum([10, 20, 30, 5, 10, 50]))
print(max_increasing_subarray_sum([10, 20, 30, 40, 50]))
print(max_increasing_subarray_sum([12, 17, 15, 13, 10, 11, 12]))
