def main():
    Q,H,S,D = map(int,input().split())
    N = int(input())
    mincos = min(4*Q,2*H,S)
    t1 = N*mincos
    t2 = (N//2)*D + (N%2)*mincos
    print(min(t1,t2))

if __name__ == '__main__':
    main()