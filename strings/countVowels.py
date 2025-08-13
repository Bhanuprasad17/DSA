text = 'bhanu prasad@123'
consonants = 0
vowels = 0
space = 0
other = 0
numbers = 0

for i in text:
    if i.lower() in 'aeiou':
        vowels += 1
    elif i.isalpha():
        consonants += 1
    elif i == ' ':
        space += 1
    elif i.isdigit():
        numbers += 1
    else:
        other += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", space)
print("Numbers:", numbers)
print("Other characters:", other)
