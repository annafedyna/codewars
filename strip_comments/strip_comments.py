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


# BETTER PRACTICE 
def solution(string,markers):
    s_list = string.split('\n')
    for marker in markers:
        s_list = [item.split(marker)[0].strip() for item in s_list]
    return '\n'.join(s_list)