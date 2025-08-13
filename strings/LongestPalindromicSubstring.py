s = 'babad'
s = 'cbbd'

def palindrom(s):
    if s == s[::-1]:
        return s
    else :
        return ''


output = []
result = ''

for i in range(0,len(s)):
    # print(s[i])
    for j in range(i+1,len(s)+1):
        str = palindrom(s[i:j])
        if len(result) < len(str) :
            result = str

print(result)