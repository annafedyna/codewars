
def isPrime(x):
    for i in range(2, int(x**0.5) +1):
        if(x % i == 0):
            return False
    return True


def gap(g, m, n):
    res = []
    for num in range(m, n+1-g):
        if isPrime(num) and isPrime(num+g):
            res += (num, num+g)
    return res if res != [] else None


print(gap(4,100,110))