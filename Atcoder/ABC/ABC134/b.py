def main():
    N,D = map(int, input().split())
    check = (N%(1+2*D))
    ans = (N//(1+2*D))
    if check == 0:
        print(ans)
    else:
        print(ans+1)

if __name__ == '__main__':
    main()