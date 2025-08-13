
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left,right)


def merge_two_sorted_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    
    while i < len_a and j < len_b :
        if a[i] <= b[j] :
            sorted_list.append(a[i])
            i += 1
        else :
            sorted_list.append(b[j])
            j += 1
    while i < len_a :
        sorted_list.append(a[i])
        i += 1
    while j < len_b :
        sorted_list.append(b[j])
        j += 1            

    return sorted_list

# arr = [10, 3, 15, 7, 8, 23, 98, 29]
arr = [9, 1, 5, 4]

print(merge_sort(arr))        

# Recursion tree for merge_sort([38, 27, 43, 3]):

#                     merge_sort([38, 27, 43, 3])
#                       /                    \
#         merge_sort([38, 27])            merge_sort([43, 3])
#            /         \                    /           \
# merge_sort([38])  merge_sort([27])  merge_sort([43])  merge_sort([3])
#      ↓                 ↓                ↓                ↓
#    [38]              [27]             [43]             [3]

#             \                         /
#         merge([38], [27])       merge([43], [3])
#                ↓                      ↓
#            [27, 38]               [3, 43]

#                      \          /
#             merge([27, 38], [3, 43])
#                           ↓
#                     [3, 27, 38, 43]

