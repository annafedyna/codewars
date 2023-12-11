from functools import reduce
from operator import add

def order_weight(strng):
    a = strng.strip().split(' ')

    res = sorted(a, key = lambda num: (reduce(add, map(int, num)), num))
    
    return ' '.join(res)

print(order_weight('2000 10003 1234000 14444 9999 11 11 22 123'))
