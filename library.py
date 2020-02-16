def isPrime(n):
    i = 2
    while True:
        if i**2 > n:
            break
        if n%i == 0:
            return False
        i += 1
    return n != 1

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact