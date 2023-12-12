from collections import deque

def max_sequence(arr):
    arr = deque(arr)
    max_sum = 0
    sub_sum = 0
    while arr:
        sub_sum += arr.popleft()
        if sub_sum < 0:
            sub_sum = 0  
        if sub_sum > max_sum :
            max_sum = sub_sum   
    return max_sum
        

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))