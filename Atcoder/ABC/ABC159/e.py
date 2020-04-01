import itertools

def main():
    H, W, K = map(int, input().split())
    S = [list(map(int,list(input()))) for _ in range(H)]
    ans = H + W - 2
    Hfind = list(itertools.product([0, 1], repeat=(H-1)))
    for i in Hfind:
        tmp = sum(i)
        now = 0
        for j in range(W):
            plus = 0
            for k in range(H):
                plus += S[k][j]
            if now+plus <= K:
                now += plus
            else:
                tmp += 1
                if plus > K:
                    break
                now = plus
        ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()