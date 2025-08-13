



arr = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicate(arr):
    result = []
    seen = set()
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result



print(remove_duplicate(arr))        