def main():
    N,K = map(int,input().split())
    R = sorted(list(map(int,input().split())))
    ls = R[-K:]
    ans = 0
    for i in range(len(ls)):
        ans = (ans+ls[i])/2
    print(ans)

if __name__ == '__main__':
    main()