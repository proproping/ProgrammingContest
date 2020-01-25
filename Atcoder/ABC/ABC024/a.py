def main():
    A,B,C,K = map(int,input().split())
    S,T = map(int,input().split())
    ans = 0
    ans += A*S + B*T
    if S+T >= K:
        ans += -C*(S+T)
    print(ans)

if __name__ == '__main__':
    main()