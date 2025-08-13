# given two dictionaries, merge them into one. If a key exists in both, sum their values

dict1 = {'k1':1,'k2':10,'k3':27,'k5':44}

dict2 = {'k3':1,'k5':10,'k9':29,'k10':44}

res_dict = {}

for i,j in dict1.items():
    res_dict[i] = j

print(res_dict)    


for i,j in dict2.items():
    if i in res_dict:
        res_dict[i] = res_dict[i] + j
    else :
        res_dict[i] = j

print(res_dict)        


# 5. swap keys and values of a dictionary. store keys in a list

dict1 = {'k1':1,'k2':10,'k3':27,'k5':44,'k6':10,'k9':27}

res_dict = {}

for i,j in dict1.items():
    res_dict[j] = i

print(res_dict)    


# given a dictionary find the key with the heighest value

dict1 = {'k1':1,'k2':10,'k3':27,'k5':44,'k6':10,'k9':27}

max_element = 'no key'
max_value = float('-inf')

for i,j in dict1.items():
    if j > max_value :
        max_value = j
        max_element = i

print(max_element)        

str1 = 'AJAY'.lower()
str2 = 'JAYA'.lower()


