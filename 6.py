import random

def Gen_PaSS(min, max):
    i = random.randint(min,max)
    password=''
    while i != 0:
        b = random.randint(33, 126)
        password = password+chr(b)
        i = i-1
    return(password)
    
passs = Gen_PaSS(7, 10)
print (passs)

