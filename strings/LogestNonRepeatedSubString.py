text = 'abccbb'
text = 'abcabcbb'
text = 'bbbbb'
text = 'pwwkew'
output = []
logest_subStr = ''

def nonRepeatedSub(str):

    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return ''
    return str        
    

for i in range(len(text)):
    for j in range(i+1,len(text)+1):
        str = nonRepeatedSub(text[i:j])
        if len(logest_subStr) < len(str):
            logest_subStr = str
          

print(logest_subStr)



