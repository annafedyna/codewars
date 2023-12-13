import functools
from operator import add

def dig_pow(n, p):
    
    sum = functools.reduce(add, [int(i)**p for i,p in zip(str(n),range(p,len(str(n))+p))])
    return sum/n if sum%n == 0 else -1 
    

print(dig_pow(695, 2))

#or similar version of my code 

def dig_pow(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1
