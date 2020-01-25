def main():
    import numpy as np
    N,M = map(int,input().split())
    ab = [np.array(list(map(int,input().split()))) for i in range(N)]
    cd = [np.array(list(map(int,input().split()))) for i in range(M)]
    ans = []
    for i in range(N):
        tmp = []
        for j in range(M):
            tmp.append(sum(list(map(abs,list(ab[i] - cd[j])))))
        ans.append(tmp.index(min(tmp)))
    for i in ans:
        print(i+1)

if __name__ == '__main__':
    main()