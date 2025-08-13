

def sumOfNum(num):
    if num == 0 :
        return 0
    return num + sumOfNum(num-1)

print(sumOfNum(5))