import math,itertools

def combinations_count(n,r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

def main():
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    odd_A = [A[i] for i in range(N) if A[i]%2 != 0]
    even_A = [A[i] for i in range(N) if A[i]%2 == 0]
    allpat = 2**N
    comb = 0
    for i in range(0,len(odd_A)+1,2):
        comb += combinations_count(len(odd_A),i)
    evenpat = (2**len(even_A))*comb
    oddpat = allpat - evenpat
    ans = oddpat if P == 1 else evenpat
    print(ans)


if __name__ == '__main__':
    main()