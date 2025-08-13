

s = "-0042"

result = 0
flage = True

for i in range(0,len(s)):
    if i == ' ':
        continue
    if i == '-':
        flage = False   
        continue
    result = result * 10 + int(s[i])


if flage == False:
    print(-result)
else :
    print(result)       

