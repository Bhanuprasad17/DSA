num1 = 20
num2 = 20
num3 = 22

if num1 == num2 == num3:
    print("All numbers are equal:", num1)
elif num1 > num2 and num1 > num3:
    print("num1 is greatest:", num1)
elif num2 > num3:
    print("num2 is greatest:", num2)
else:
    print("num3 is greatest:", num3)


