


# def move_zeroes_to_end(nums):
    
#     result = []
#     count = 0

#     for num in nums:
#         if num != 0:
#             result.append(num)
#         else:
#             count += 1 

#     print("Count of zeroes:", count)   
#     print("Resulting list:", result + [0] * count)
    
# move_zeroes_to_end([0, 1, 0, 3, 12])    



def move_zeroes_to_end(arr):
    position = 0  # This is where the next non-zero should go

    for current in range(len(arr)):
        if arr[current] != 0:
            arr[position] = arr[current]
            position += 1

    # Fill remaining positions with 0
    while position < len(arr):
        arr[position] = 0
        position += 1

    return arr


print(move_zeroes_to_end([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]


