import re
# Solution 1 
def increment_string(strng):
    
    num = re.findall('[0-9]+$', strng)
    
    if num:
        num = num[0] 
        return re.sub('[0-9]+$', str(int(num) + 1).zfill(len(num)), strng)
    else :
        return strng + str(1)
   
 # Solution 2  
 
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

print(increment_string('foo7bar000099'))