num = 121

temp = num
result = 0

while temp > 0 :
    rem = temp % 10
    result = result * 10 + rem
    temp = temp // 10
    
if result == num :
    print(f'{num} is palindrome')
else :
    print(f'{num} is not palindrome')
