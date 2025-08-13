def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    i = j = 0
    len_a = len(nums1)
    len_b = len(nums2)
    
    output_list = []
    
    while i < len_a and j < len_b:
        if nums1[i] < nums2[j]:
            output_list.append(nums1[i])
            i += 1
        else:
            output_list.append(nums2[j])
            j += 1
    
    while i < len_a:
        output_list.append(nums1[i])
        i += 1
    
    while j < len_b:
        output_list.append(nums2[j])
        j += 1
    
    if len(output_list) % 2 != 0:
        median = len(output_list) // 2
        result = float(output_list[median])
    else:
        median = len(output_list) // 2
        result = float(output_list[median] + output_list[median - 1]) / 2
    
    # Return as float with 5 decimal precision
    return round(result)


print(findMedianSortedArrays([1,2],[3,4]))

from decimal import Decimal

num = 2.5
print(num)

str_value = "0000"
s = str(num) + str_value
n = Decimal(s)
print(type(n))