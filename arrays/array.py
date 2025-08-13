# Given an array of positive integers, find the number of subarrays of size k 
# whose average is greater than or equal to a given threshold.

arr = [2,1,3,4,1,2,1,5,20]
k = 3
threshold = 3

count = 0
window_sum = sum(arr[:k])

if window_sum / k >= threshold :
    count += 1
   
for i in range(k,len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    if window_sum / k >= threshold:
        count += 1

print(count)