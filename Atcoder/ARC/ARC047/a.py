def main():
    N,L = map(int,input().split())
    S = list(input())
    crash = 0
    tab = 1
    for i in range(N):
        if S[i] == "+":
            tab += 1
            if tab > L:
                crash += 1
                tab = 1
        else:
            tab -= 1
    print(crash)

if __name__ == '__main__':
    main()