def odd_series_upto_a(a):
    result = []
    num = 1
    for _ in range(a):
        result.append(num)
        num += 2
    return result


print("Series:", odd_series_upto_a(4)) 
