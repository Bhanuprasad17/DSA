

# def fact(num):
#     if num in [0,1]:
#         return 1
#     return num * fact(num-1)

# print(fact(5))


# name = 'madam'
# print(name[:-1])

# temp = name


# def reverse_string(str):
#     if len(str) <= 1:
#         return str
#     return str[-1] + reverse_string(str[:-1])

# # print(reverse_string(temp))
# res = reverse_string(temp)

# if res == name :
#     print(f'{name} is palindrom')
# else :
#     print(f'{name} is not panlindrom')


# def sumOfDigits(num):
#     if num == 0 :
#         return 0
#     return num%10 + sumOfDigits(num//10)

# print(sumOfDigits(64342))


# def sumOfList(list):
#     if len(list) == 0 :
#         return 0
#     if len(list) == 1:
#         return list[0]
#     return list[0] +sumOfList(list[1:])

# print(sumOfList([1,2,3,4]))
# print(sumOfList([]))

# def sumOfN(num):
#     if num == 0 :
#         return 0
#     return num + sumOfN(num-1)

# print(sumOfN(5))

# def fibnocci(num):
#     if num == 0 :
#         return 0
#     if num == 1:
#         return 1
#     return fibnocci(num-1) + fibnocci(num-2)

# # print(fibnocci(5))

# for i in range(0,10):
#     print(fibnocci(i),end=' ')

print(2//2)