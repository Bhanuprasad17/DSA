


arr =  [1, 2, 2, 3, 4, 4, 5] 


def uniqueNums(arr):

    dict = {}

    for i in arr:
        if i in dict:
            dict[i] = dict[i] + 1
        else :
            dict[i] = 1

    result = []

    for key,value in dict.items():
        if value == 1:
            result.append(key)

    return result


print(uniqueNums(arr))
                    