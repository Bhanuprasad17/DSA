

x = 1534236469
x = -123
x = 123

min_int = -2**31
max_int = 2**31 - 1

result = 0
flage = True
if x < 0 :
    flage = False
    x = abs(x)
    
# print(x)    

while x != 0 :
    rem = x % 10
    x = x // 10
    result = result * 10 + rem

if flage == False :
    result = -result


if result < min_int or result > max_int :
    result = 0


print(result)

