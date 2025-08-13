


def find_missing_number(arr,n):

    total = (n*(n+1))//2
    # print(sum)
    actual_sum = sum(arr)

    return total-actual_sum

print(find_missing_number([3,0,1],3)) 
print(find_missing_number([1, 2, 4, 6, 3, 7, 8],8)) 

