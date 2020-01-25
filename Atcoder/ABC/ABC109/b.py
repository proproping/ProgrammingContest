def main():
    N = int(input())
    W = [input() for i in range(N)]
    ans = "Yes"
    if sorted(set(W)) != sorted(W):
        ans = "No"
    else:
        for i in range(N-1):
            if W[i][-1] != W[i+1][0]:
                ans = "No"
                break
    print(ans)

if __name__ == '__main__':
    main()