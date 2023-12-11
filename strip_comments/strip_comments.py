import re

def strip_comments(strng, markers):
    for marker in markers:
        strng = re.sub(rf'{re.escape(marker)}.*', '', strng)
    return re.sub(r'\s*$', '', strng, flags=re.MULTILINE)

result = strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
print(result)