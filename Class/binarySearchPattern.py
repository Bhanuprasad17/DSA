def binary_search(arr, target):
    
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found in the array

binary_search_result = binary_search([2, 4, 6, 8, 10, 12, 14], 10)
print(binary_search_result)  # Output: 2 (index of the target in the array)