


def kth_distinct_string(arr,k):

    freq = {}
    for i in arr:
        if i in freq:
            freq[i] = freq[i] + 1
        else :
            freq[i] = 1

    for i in arr:
        if freq[i] == 1 :
            k = k - 1
            if k == 0 :
              return i

    return ""                               

print(kth_distinct_string(["d", "b", "c", "b", "c", "a"], 2))
print(kth_distinct_string(["aaa", "aa", "a"], 1)) 
print(kth_distinct_string(["a", "b", "a"], 3))