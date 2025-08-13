arr = [1, 2, 1, 3, 4, 2, 3]
#      0  1  2  3  4  5  6
k = 3

count = 0

for i in range(len(arr)-k + 1):
    # print(i)
    window = arr[i : i+k]
    if k == len(set(window)):
        count += 1

print(count)

# print()
    