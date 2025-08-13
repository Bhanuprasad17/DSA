# Given a string text = "abcde" and a fixed window size k = 3, print all substrings of length 3


text = "abcdef"

k = 3
n = len(text)

for i in range(n - k + 1):
    substring = text[i:i + k]
    print(substring)