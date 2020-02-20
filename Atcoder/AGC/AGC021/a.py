def main():
    N = int(input())
    if N < 10:
        print(N)
    elif str(N)[1:] == "9"*(len(str(N))-1):
        print(sum(list(map(int,list(str(N))))))
    else:
        ans = sum([9]*(len(str(N))-1))
        if int(str(N)[0]) >= 2:
            ans += int(str(N)[0])-1
        print(ans)

if __name__ == '__main__':
    main()