# Longest Substring Without Repeating Characters

text = "abcabcbb"
def longest_unique_substring(text) :

    seen = {}
    start = 0
    max_length = 0