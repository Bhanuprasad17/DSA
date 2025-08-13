# def rotate(self, nums, k):
#         n = len(nums)
#         k = k % n

#         def reverse(start, end):
#             while start < end:
#                 nums[start], nums[end] = nums[end], nums[start]
#                 start += 1
#                 end -= 1

#         reverse(0, n - 1)
#         reverse(0, k - 1)
#         reverse(k, n - 1)

#         return nums


# print(11%7)

nums = [1,2,3,4,5,6]

def reverse(start,end):
    while start < end :
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1


reverse(0,len(nums)-1)
print(nums)