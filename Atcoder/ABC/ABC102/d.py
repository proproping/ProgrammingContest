from itertools import accumulate
def main():
    N = int(input())
    A = list(map(int,input().split()))
    cumsum = list(accumulate(A))
    cutindex = []
    limit = cumsum[-1]/2
    for i in range(1,N):
        if cumsum[i] >= limit:
            if abs(limit-cumsum[i]) >= abs(limit-cumsum[i-1]):
                cutindex.append(i)
            else:
                cutindex.append(i+1)
            break
    print(cutindex)


if __name__ == '__main__':
    main()