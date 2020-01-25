def main():
    N = int(input())
    c = list(range(0,int(N/4)+1))
    d = list(range(0,int(N/7)+1))
    ans = "No"
    for i in range(len(c)):
        for j in range(len(d)):
            if N - (4*i + 7*j) == 0:
                ans = "Yes"
                break
    print(ans)

if __name__ == '__main__':
    main()