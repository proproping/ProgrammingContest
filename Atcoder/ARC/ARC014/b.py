from collections import defaultdict

def main():
    N = int(input())
    dic = defaultdict(int)
    ans = "DRAW"
    W = [input() for _ in range(N)]
    dic[W[0]] = 1
    last = W[0][-1]
    for i in range(1,N):
        if (dic[W[i]] == 0) and (last == W[i][0]):
            dic[W[i]] += 1
            last = W[i][-1]
        else:
            ans = "LOSE" if i%2 == 0 else "WIN"
            break
    print(ans)

if __name__ == '__main__':
    main()