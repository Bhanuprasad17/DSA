


str1 = 'bhanu'

def reverseStr(str):
    if len(str) <= 1:
        return str
    return str[-1] + reverseStr(str[:-1])

print(reverseStr('bhanu'))



str1 = "Bhanu"
def rev_str(s):
    if len(s) <= 1:
        return s
    return s[-1] + rev_str(s[:len(s)-1])    

print(rev_str(str1))   