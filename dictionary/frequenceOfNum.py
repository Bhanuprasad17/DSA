# 1.given list of numbers, count the occurrences of each number and return a dictionary

list1 = [1,2,1,3,2,2,'str','str',5,7]

dict = {}


for i in list1:
    if i in dict:
        dict[i] = dict[i] + 1
    else :
        dict[i] = 1


print(dict)            


# 2.Given list of words
# return a dictionary where the keys are words and values are thier length

list1 = ['apple','ball','bat']

dict = {}

for i in list1:
    dict[i] = len(i)

print(dict)    

# Given a string 
# return a dictionary where keys are characters and values are their frequences

