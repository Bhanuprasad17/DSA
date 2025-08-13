text = 'abccbb'
output = []

def nonRepeatedSub(str):

    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return False
    return True        
    

for i in range(len(text)):
    for j in range(i+1,len(text)+1):
        print(text[i:j])
        flage = nonRepeatedSub(text[i:j])
        if flage == True:
            output.append(text[i:j])

print(output)            



