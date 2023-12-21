

def next_bigger(n):
    n_list = list(str(n))
    
    for i in range(len(n_list)-1 , 0, -1):
        if n_list[i] > n_list[i-1]:
            tail = n_list[i-1:]
            min_el = min(filter(lambda x: x > tail[0],tail))
            tail.remove(min_el)
            tail.sort()
            return int(''.join(n_list[:i-1] + [min_el] + tail))
            
    return -1

print(next_bigger(534976))