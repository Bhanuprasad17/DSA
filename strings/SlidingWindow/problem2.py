# Longest substring with all unique characters of length k


text = "abcabcbb"
k = 3

for i in range(len(text) - k + 1):
    window = text[i:i + k]
    if len(set(window)) == k:
        print("Unique window:", window)