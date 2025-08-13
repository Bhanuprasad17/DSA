text = 'madam'.lower()
rev_str = ''

n = len(text)

for i in range(n):
    rev_str += text[n-i-1]

if rev_str == text:
    print(f'{text} is palindrome')
else :
    print(f'{text} is not palindrome')


# Two pointer approach 

def is_palindrome(str1):
    left = 0
    right = len(str1) - 1
    while left < right :
        if(str1[left] != str1[right]):
            return False
        left = left + 1
        right = right - 1
    return True
    
print(is_palindrome("madam"))  
print(is_palindrome("hello"))