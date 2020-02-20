import itertools

def main():
    N,x = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    accum_a = list(itertools.accumulate(a))
    ans = 0
    for i in range(N):
        if accum_a[i] > x:
            break
        else:
            ans += 1
    if accum_a[-1] < x:
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()