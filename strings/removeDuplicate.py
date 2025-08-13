text = 'dell'
result = ''

# for i in text:
#     if i not in result:
#         result += i

# print(result)        


for i in range(len(text)):
    found = False
    
    for j in range(len(result)):
        if text[i] == result[j]:
            found = True
            break
    if not found:
        result += text[i]    

print(result)