nums = [1,2,3,4,5,6]

def reverse(start,end):
    while start < end :
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1


reverse(0,len(nums)-1)
print(nums)