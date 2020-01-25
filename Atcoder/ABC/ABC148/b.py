def main():
    N = int(input())
    S,T = map(str,input().split())
    tmp = []
    for i in range(N):
        tmp.append(S[i])
        tmp.append(T[i])
    print(*tmp,sep="")

if __name__ == '__main__':
    main()