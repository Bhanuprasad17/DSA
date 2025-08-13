


def missing_num_arr(arr):
    
    n = len(arr)
    total_sum = (n * (n + 1)) // 2  # Sum of first n natural numbers
    arr_sum = sum(arr)  # Sum of elements in the array
    missing_num = total_sum - arr_sum  # The missing number is the difference
    return missing_num

print(missing_num_arr([0, 1, 2, 3, 5]))  # Output: 4