from itertools import product    

def get_pins(observed):
    d = [
        ['0','8'],
        ['1','4','2'],
        ['2', '1', '3', '5'],
        ['3','2','6'],
        ['4','1','7','5'],
        ['5','2', '4','8', '6'],
        ['6', '3', '5', '9'],
        ['7','4', '8'],
        ['8', '5', '7','9','0'],
        ['9','6', '8'],
    ]

    return [''.join(pin) for pin in product(*(d[int(num)] for num in observed))]


print(get_pins('36'))