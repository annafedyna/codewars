
def isPrime(x):
    for i in range(2, int(x**0.5) +1):
        if(x % i == 0):
            return False
    return True


def gap(g, m, n):
    primes_num = []
    for num in range(m, n+1):
        if isPrime(num): primes_num.append(num)
        
    for i in range(len(primes_num)-1):
        if abs(primes_num[i] - primes_num[i+1]) == g:
            return [primes_num[i], primes_num[i+1]]


print(gap(4,100,110))