arr = [2, 5, 1, 7, 10]
k = 14

largest_sum = 0

for i in range(len(arr)):
    current_sum = 0
    for j in range(i+1, len(arr)):
        # print(arr[i:j])
        current_sum += arr[j]
        if current_sum <= k and current_sum > largest_sum:
            largest_sum = current_sum

print("Largest subarray sum <= k is:", largest_sum)
