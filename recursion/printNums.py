num = 10

def print_num(num):
    if num < 0:
        return
    print(num)
    return print_num(num - 1)

print_num(num)
