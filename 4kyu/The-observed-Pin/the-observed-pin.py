from itertools import product    

def combinations(*arrays):
    return list(product(*arrays))

def get_pins(observed):
    d = [
        ['1','4','2'],
        ['2', '1', '3', '5'],
        ['3','2','6'],
        ['4','1','7','5'],
        ['5','2', '4','8', '6'],
        ['6', '3', '5', '9'],
        ['7','4', '8'],
        ['8', '5', '7','9','0'],
        ['9','6', '8'],
        ['0','8']
    ]
    
    arrays = []
    for i in range(len(observed)):
        for j in range(len(d)):
            if observed[i] == d[j][0]:
                arrays.append(d[j])
    
    res = combinations(*arrays)

    return [''.join(a) for a in res]


print(get_pins('36'))