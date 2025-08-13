# dict = {
#     1 : 'bhanu',
#     2 : 'Dell',
#     3 : 'gram',
#     1 : 'bhanuprasd',
#     'name':'bhanupasad',
#     4:5
# }
# # Keys should be unique 
# print(dict)
# print(dict[1])
# print(dict['name'])

# dict[4] = dict[4] + 1
# print(dict)

# dict[5] = 10
# print(dict)

# dict[6] = dict[6] + 1 # error 
# print(dict)


dict = {
    "name" : "Bhanuprasad",
    "age" : 23,
    "rollno" : 123,
    "marks" : [90, 80, 70],
}

print(dict)
print(dict['name'])
print(dict['marks'])

dict['name'] = 'kohli'
dict['age'] = 38
# print(dict['city']) # keyerror
# del dict['age']
value = dict.pop('age')
print(value)
print(dict)

for key in dict:
    print(key)
for value in dict.values():
    print(value)
for key,value in dict.items():
    print(key , ':' , value)

print(dict['marks'][0])    
    



dict = {
    "name" : 'bhanu',
    "age" : 23,
    "address" : {
        "city" : 'hyderabad',
        "state" : 'Telangana'
    }
}

print(dict)
print(dict['name'])
print(dict['age'])
print(dict['address'])

dict['name'] = 'kohli'
dict['age'] = 48

print(dict)
print(dict['address']['city'])
dict['address']['city'] = 'mumbai'


for key in dict:
    print(key)
    
for value in dict.values():
    print(value)
    
    
for key,value in dict.items():
    print(key ,":", value)
    
    