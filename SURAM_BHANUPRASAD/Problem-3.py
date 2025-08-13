def conditional_odd_series(a):
    result = []
    num = 1
    for i in range(1, a + 1):
        if a % 2 != 0:
            result.append(num)
            num += 2
        elif i % 2 != 0:
            result.append(num)
            num += 2
    return result

print("Series:", conditional_odd_series(4))  