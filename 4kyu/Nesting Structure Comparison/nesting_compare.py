def same_structure_as(original, other):
    if not isinstance(original, list) or not isinstance(other, list):
        return False

    if len(original) != len(other):
        return False

    for i in range(len(original)):
        if type(original[i]) == type(other[i]) == list:
            return same_structure_as(original[i], other[i])
        elif bool(type(original[i])== list )!= bool(type(other[i])==list):
            return False

    return True


print(same_structure_as([1,'[',']'],['[',']',1]))

print(same_structure_as([ [ [], [] ] ],   [ [ [], [] ] ] ))

# BEST PRACTICE

def same_structure(original, other):
    return type(original) == type(other) and (len(original) == len(other) and all(map(same_structure,original, other))) if type(original) == list else 1

print(same_structure([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ]))

print(same_structure([ [ [], [] ] ],   [ [ [], [] ] ] ))