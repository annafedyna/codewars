def isPrime(x):
    if (x < 2) or (x % 2 ==0): return False
    for i in range(3, int(x**0.5),2):
        if x % i == 0: return False
    return True

def gap(g, m, n):
    prev_prime = n
    for num in range(m, n+1):
        if isPrime(num):
            if num - prev_prime == g:
                return [prev_prime,num]
            prev_prime = num
             
print(gap(4,100,110))