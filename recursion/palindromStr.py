

def reverseStr(str):
    if len(str) <= 1:
        return str
    return str[-1] + reverseStr(str[:-1])


str = 'bhanu'
temp = str
res = reverseStr(temp)

if res == str :
    print(f'{str} is palindrom')
else :
    print(f'{str} is not palindrom')    



    