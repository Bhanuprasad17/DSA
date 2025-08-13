
# Function to find the maximum sum of a fixed-size sliding window in an array

def max_sum_fixed_window(arr, k):

    window_sum = sum(arr[:k])  # Initial sum of the first 'k' elements
    max_sum = window_sum
    n = len(arr)

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum

print(max_sum_fixed_window([1, 2, 3, 4, 5], 3))  # Should return 12 (sum of [3, 4, 5])