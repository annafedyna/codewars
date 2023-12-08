from functools import reduce
from operator import add
from collections import OrderedDict

def order_weight(strng):
    a = strng.strip().split(' ')

    weights = [reduce(add, map(int, num)) for num in a]

    d = OrderedDict()
    for i in range(len(weights)):
        d[weights[i]] = a[i]

    sorted_keys = sorted(d.keys())
    res = [d[key] for key in sorted_keys]

    return ' '.join(res)

print(order_weight('2000 10003 1234000 14444 9999 11 11 22 123'))