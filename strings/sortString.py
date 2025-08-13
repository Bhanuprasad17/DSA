# text = 'Bhanu'.lower()

# sorted_list = sorted(text)
# print(sorted_list)
# sorted_list = ''.join(sorted_list)
# print(sorted_list)

# Bubble Sort implementation for sorting characters in a string

text = 'Bhanu'.lower()

char_list = list(text)

n = len(char_list)

for i in range(n-1):
    for j in range(n-i-1):
        if char_list[j] > char_list[j+1]:
            char_list[j], char_list[j+1] = char_list[j+1], char_list[j]

print(''.join(char_list))            