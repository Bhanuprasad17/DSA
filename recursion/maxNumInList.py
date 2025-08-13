

list1 = [2.2, 55, 4567, -112, 32, 234]

def max_elem(list1):
    if len(list1) == 0:
        return 'No Max'
    elif len(list1) == 1:
        return list1[0]
    res = max_elem(list1[1:])

    return res if res > list1[0] else list1[0]

print(max_elem(list1))