text = 'Bhanu'

n = len(text)

k = 1 % n

for i in range(k):
    lastword = text[n-1]
    text_list = list(text)
    for i in range(len(text_list)-1,0,-1):
        text_list[i] = text_list[i-1]
    text_list[0] = lastword    
    text = ''.join(text_list)

print(text)    
    

# Output: uBhan