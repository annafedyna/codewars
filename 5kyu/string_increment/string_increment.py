import re

def increment_string(strng):
    
    num = re.findall('[0-9]+$', strng)
    
    if num:
        num = num[0] 
        return re.sub('[0-9]+$', str(int(num) + 1).zfill(len(num)), strng)
    else :
        return strng + str(1)

print(increment_string('foobar0099'))