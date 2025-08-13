str1 = 'take you forward is awesome'.lower()

# for i in str1:
#     if str1.count(i) == 1 and i in'aeiou':
#         print(i)

def countAlpha(str1,char):
    count = 0
    for i in str1:
        if i == char:
            count += 1
    return count        


# for i in 'aeiou':
#     if str1.count(i) == 1:
#         print(i)


for i in 'aeiou':
    if  countAlpha(str1,i)== 1:
        print(i)