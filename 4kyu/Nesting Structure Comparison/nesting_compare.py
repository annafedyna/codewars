def same_structure_as(original, other):
    if not isinstance(original, list) or not isinstance(other, list):
        return False

    if len(original) != len(other):
        return False

    for i in range(len(original)):
        if type(original[i]) == type(other[i]):
            if type(original[i]) == list:
                if not same_structure_as(original[i], other[i]):
                    return False
        else:
            return False

    return True


print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ]))

print(same_structure_as([ [ [], [] ] ],   [ [ [], [] ] ] ))


# This code fails:  [1,'[',']'] same as ['[',']',1]: False should equal True
