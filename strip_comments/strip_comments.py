import re

def strip_comments(strng, markers):
    lines = re.split('\n', strng)
    print(lines)
   
    arr = []
    for line in lines:
        
        for marker in markers:
            line = re.sub(rf'{re.escape(marker)}.*', '', line)
            
        line = re.sub(r'^\s*$', '', line)
        arr.append(line)
        
    return '\n'.join(arr)

result = strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
print(result) 