import itertools

def main():
    N = int(input())
    t = [int(input()) for _ in range(N)]
    ls = list(itertools.product([0,1],repeat=N))
    sumt = sum(t)
    ans = 10**9
    for i in ls:
        tmp = 0
        for j in range(N):
            tmp += t[j]*i[j]
        ans = min(ans,max(tmp,sumt-tmp))
    print(ans)

if __name__ == '__main__':
    main()