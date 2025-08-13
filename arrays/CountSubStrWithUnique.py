s = "abcabcbb"
k = 3

count = 0
for i in range(len(s)-k + 1):
    # print(i)
    window = s[i:i+k]
    if len(window) == len(set(window)):
        # count += 1
        print(window)


