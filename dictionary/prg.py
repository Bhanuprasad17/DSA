dict1 = {'k1':1,'k2':10,'k3':27,'k5':44}

dict2 = {'k3':1,'k5':10,'k9':29,'k10':44}

res_dict = {}


for i,j in dict1.items():
    # print(i,j)
    res_dict[i] = j

print(res_dict)    

for i,j in dict2.items():
    if i in res_dict:
        res_dict[i] = res_dict[i] + j
    else :
        res_dict[i] = j    

print(res_dict)        