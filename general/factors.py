# Factors of a number
def perfectNum(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            # factors.append(i)
            total += i
    return total

number = 28
print(perfectNum(28))


