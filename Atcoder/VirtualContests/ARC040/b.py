def main():
    N,R = map(int,input().split())
    S = list(input())
    ans = 0
    shot = True
    for i in range(N-1,-1,-1):
        if S[i] == ".":
            for j in range(max(0,i-R+1),i+1):
                S[j] = "o"
            ans += 1
            if shot:
                ans += max(0,i-R+1)
                shot = False
    print(ans)

if __name__ == '__main__':
    main()