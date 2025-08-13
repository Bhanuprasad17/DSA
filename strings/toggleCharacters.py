print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
print(chr(ord('a')-32))
print(chr(ord('A')+32))


text = 'BhAnu PRasAd'
result = ''

# for i in text:
#     if i == ' ':
#         result += ' '
#     if ord(i) >= 65 and ord(i) <= 90 :
#         result += chr(ord(i)+32)
#     if ord(i) >= 97 and ord(i) <= 122:
#         result += chr(ord(i)-32)
# print(result)    


for i in text:
    if i == ' ':
        result += ' '
    elif i >= 'A' and i <= 'Z':
        result += chr(ord(i)+32)
    else:
        result += chr(ord(i)-32)    
print(result)



# ------------------------------------------------------------------------------------


print(ord('A'))  # 65
print(ord('a'))  # 97
print(chr(ord('A')+32))    
print(chr(ord('a')-32))

def toggleCharacter(s):
    
    result = ''
    for i in s:
        if i == ' ':
            result += ' '
        elif i >= 'A' and i <= 'Z':
            result = result + chr(ord(i)+32)
        else :
            result = result + chr(ord(i)-32)
    return result 
    
print(toggleCharacter('BhAnu PRasAd'))    
print(toggleCharacter('Hello 123!'))    
            


# --------------------------------------------------------------------------------
def toggleCharacter(s):
    result = ''
    for i in s:
        if i.isupper():
            result = result + i.lower()
        elif i.islower():
            result = result + i.upper()
        else :
            result = result + i
    return result 
    
print(toggleCharacter('BhAnu PRasAd'))      
print(toggleCharacter('Hello 123!'))     

