def format_duration(s):
    duration_dict = {
        'seconds' : s%60,
        'minutes' : (s//60)%60,
        'hours' : (s//3600)%24,
        'days' : ((s//3600)//24)%365,
        'years' : ((s//3600)//24) //365
    }
    a = list(reversed([(value, k if value > 1 else k[:len(k)-1]) for k,value in duration_dict.items() if value > 0]))
    
    res = ''
    for i in range(len(a)):
        num, unit = a[i]
        res += f'{num} {unit}'
        if i != len(a) -2 and i != len(a)-1:
            res += ', '
        elif i == len(a) -2:
            res += ' and '
    
    return res
    
    
    
print(format_duration(3662))