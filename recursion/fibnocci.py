

def fib(num):
    n1 = 0
    n2 = 1
    print(n1, n2, end=' ')
    for i in range(2,num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3,end=' ')

fib(4)        


def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

# for i in range(10):
#     print(fibonacci(i), end=' ')

print(fibonacci(1))





    