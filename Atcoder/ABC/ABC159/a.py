def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def combinations_count(n,r):
    return fact(n) // (fact(n - r) * fact(r))

def main():
    N, M = map(int, input().split())
    ans = 0
    if N >= 2:
        ans += combinations_count(N, 2)
    if M >= 2:
        ans += combinations_count(M, 2)
    print(ans)

if __name__ == '__main__':
    main()