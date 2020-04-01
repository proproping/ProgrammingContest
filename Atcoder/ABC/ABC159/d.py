from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    comb = 0
    for i in c.values():
        if i >= 2:
            comb += i*(i-1)//2
    for i in range(N):
        print(comb - (c[A[i]] - 1))

if __name__ == '__main__':
    main()