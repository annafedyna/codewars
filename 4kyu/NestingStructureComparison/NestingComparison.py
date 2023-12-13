def same_structure_as(original,other):
    
    for i in range(len(original)):
        for j in range(len(other)):
            if type(original[i]) == type(other[j]):
                if type(original[i]) == list:
                    return same_structure_as(original[i],other[j])
                else:
                    return False



print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ]))

print(same_structure_as([ [ [], [] ] ],   [ [ [], [] ] ] ))


# This code fails:  [1,'[',']'] same as ['[',']',1]: False should equal True