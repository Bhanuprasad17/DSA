# arr = [5,9,1,8,7]

# largest_sum = float('-inf')

# # sum = 0
# for i in range(0,len(arr)-2):
#     sum = 0
#     for j in range(i,i+3):
#         sum = sum + arr[j]
#     if sum > largest_sum :
#         largest_sum = sum

# print(largest_sum)   
# O(n^2)     


# arr = [5,9,1,8,7]
# k = 3

arr = [-1,2,3,3,4,5,-1]
k = 4

window_sum = sum(arr[:k])
largest_sum = window_sum

for i in range(k,len(arr)-1):
    window_sum += arr[i] - arr[i-k]
    largest_sum = max(window_sum,largest_sum)

print(largest_sum)    



# arr = [-1,2,3,3,4,5,-1]
# k = 4

# window_sum = sum(arr[:k])
# # print(window_sum)
# max_sum = window_sum

# for i in range(k-1):
#     # print(i)
#     window_sum = window_sum - arr[i] + arr[k+i]
#     if max_sum < window_sum :
#         max_sum = window_sum
#     # print(window_sum)
    
# print(max_sum)   





# ---------------------------------------------------------------------------------------------------------





arr = [3,1,4,1,5,9]
max_num = float('-inf')
second_max = float('-inf')
third_max = float('inf')

for i in arr:
    # print(i)
    if i > max_num :
        third_max = second_max
        second_max = max_num
        max_num = i
    elif i != max_num and i > second_max :
        second_max = i
    elif i != second_max and i > third_max :
        third_max = i

print(max_num)        
print(second_max)
print(third_max)


# https://docs.google.com/document/d/1UlYlpxO6cAgZ0Eav1P5y7rzuVw8rL8ZgC9VVFIEpqWI/edit?tab=t.0