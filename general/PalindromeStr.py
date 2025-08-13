text = 'madam'.lower()
rev_str = ''

n = len(text)

for i in range(n):
    rev_str += text[n-i-1]

if rev_str == text:
    print(f'{text} is palindrome')
else :
    print(f'{text} is not palindrome')
    
    