def count_multiples(lst):
    result = {}
    for i in range(1, 10):
        result[i] = sum(1 for num in lst if num % i == 0)
    return result


data = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print("Multiples count:", count_multiples(data))
