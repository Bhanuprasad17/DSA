l = [1,2,3,4,5,6,7,8] # [1,(2,3),{4,5},(6,7,10)]
l[1:3] = [tuple(l[1:3])]
print(l)

# ------------------------------------------------

l = [x for x in range(10)]
l = [x for x in range(10) if x%2 == 0]
l = [x for x in range(10) if x%2 == 0]
print(l)
l = [[x] for x in range(10) if x%2 == 0]
print(l)
print(*l)

# ------------------------------------------------

k = {'a':1,'b':2,'c':3,'d':4,'e':5}
l = {x:y for x,y in k.items() if y%2 == 0}
l = {x:y*2  for x,y in k.items() if y%2 == 0}
print(l)


l = {x:(y*2 if y % 2 == 0 else y ) for x,y in k.items()}
print(l)

l = {x:(y-10 if y % 2 != 0 else y ) for x,y in k.items()}
print(l)

#------------------------------------------------


l = 'Python Developer'

print(chr(ord('A')+32))
print(ord(l[0]))
print(65+26)

result = ''

for i in l:
    if i == ' ':
        result = result + ' '
    if ord(i) >= 65 and ord(i) <= 91:
        result += chr(ord(i)+32)
    else :
        result += chr(ord(i)-32)

print(result)      


# --------------------------------------------------


# factors of a number

n = 20

for x in range(1,n):
    if n % x == 0 :
        print(x)


# --------------------------------------------------

n = 5 


def fact(n):
    if n in [0,1]:
        return 1
    return n * fact(n-1)

print(fact(n))


# ---------------------------------------------------
# Armstrong number
# Aito - 5

n = 25
expo = n**2
l = len(str(expo))


if expo % 10 == n :
    print(n)


print(20020 % 100)    

# ----------------------------------------------------

k = 8
l = '0123456789'
res = ''

for x in range(len(l)):
    if k == x :
        res += l[x]

print(res)        
print(type(res))

# ------------------------------------------


k = 12
l = '0123456789'
res = ''

for x in range(len(l)):
    if k == x :
        res += l[x]

print(res)        
print(type(res))


# ----------------------------------------------------
# string to number


