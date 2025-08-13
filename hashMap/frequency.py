

s = "aabbcde"
s = "aabbcc"
s = "xxyyzzd"
s = "abcabcabc"

freq = {}


for i in s :
    if i in freq:
        freq[i] = freq[i] + 1
    else :
        freq[i] = 1

print(freq)        


for key,value in freq.items():
    if value == 1:
        print(key)
        break
        
