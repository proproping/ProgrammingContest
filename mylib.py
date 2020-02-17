# O(log max(a,b))
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

# O(log max(a,b))
def extgcd(a,b,x,y):
    d = a
    if b != 0:
        d = extgcd(b,a%b,y,x)
        y -= (a//b)*x
    else:
        x,y = 1,0
    return d

# O(log max(a,b))
def lcm(a,b):
    return (a*b)//gcd(a,b)

# O(n)
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def permutaions_count(n,r):
    return fact(n) // fact(n-r)

def combinations_count(n,r):
    return fact(n) // (fact(n-r) * fact(r))

# O(√n)
def isPrime(n):
    i = 2
    while True:
        if i**2 > n:
            break
        if n%i == 0:
            return False
        i += 1
    return n != 1

# O(√n)
def divisor(n):
    res = []
    i = 1
    while True:
        if i**2 > n:
            break
        if n%i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
        i += 1
    return res

# O(√n)
def prime_factor(n):
    res = {}
    i = 2
    while True:
        if i**2 > n:
            break
        while n%i == 0:
            if not i in res.keys():
                res[i] = 1
            else:
                res[i] += 1
            n //= i
        i += 1
    if n != 1:
        res[n] = 1
    return res

# O(n log log n)
def sieve(n):
    prime = [-1]*n
    is_prime = [True]*(n+1)
    p = 0
    is_prime[0] = is_prime[1] = False
    for i in range(2,n+1):
        if is_prime[i]:
            prime[p] = i
            p += 1
            for j in range(2*i,n+1,i):
                is_prime[j] = False
    return p

# O(n log log n)?
def segment_sieve(a,b):
    import math
    is_prime = [True]*(b-a)
    is_prime_small = [True]*math.ceil(math.sqrt(b))
    is_prime_small[0] = is_prime_small[1] = False
    for i in range(2,len(is_prime_small)):
        if is_prime_small[i]:
            for j in range(2*i,len(is_prime_small),i):
                is_prime_small[j] = False
            for j in range(max(2,(a+i-1)//i)*i,b,i):
                is_prime[j-a] = False
    return sum(is_prime)

# O(log n) <-> pow(x,n,mod)
def mod_pow(x,n,mod):
    if n == 0:
        return 1
    res = mod_pow(x*x%mod,n//2,mod)
    if n & 1:
        res = res*x%mod
    return res

def to_k_base_num(n,k):
    bi = ""
    while n != 0:
        bi += str(n%abs(k))
        if k < 0:
            n = -(-n//k)
        else:
            n //= k
    return bi[::-1]

