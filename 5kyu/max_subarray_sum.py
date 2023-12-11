from collections import deque

def max_sequence(arr):
    arr = deque(arr)
    max = 0
    for i in range(len(arr)):
        sub_sum = 0
        for j in range(len(arr)):
            sub_sum = sub_sum + arr[j]
            if max < sub_sum:
                max = sub_sum
        
        arr.popleft()
    return max
        

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))