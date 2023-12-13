def next_bigger(n):
    n_list = list(str(n))
    fs = None
    
    for i in range(len(n_list) - 1, 0, -1):
        if n_list[i] > n_list[i - 1]:   
            fs = n_list[i -1]
            index = i-1
            break
            
    if not fs:
        return -1

    right = sorted([n_list[j] for j in range(len(n_list)-1,index,-1)])
    fss  = fs
    for e in range(len(right)):
        if right[e] > fs:
            fs = right[e]
            right[e] = fss
            break
    
    res = [n_list[i] for i in range(index)] + [fs] + right
    return int(''.join(res))

print(next_bigger(534976))