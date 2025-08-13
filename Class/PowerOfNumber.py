 

def power_of_number(base, exponent):
    result = 1

    for _ in range(exponent):
        result *= base
    return result

print(power_of_number(2, 5))  # Output: 32


def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 5))  # Output: 32    