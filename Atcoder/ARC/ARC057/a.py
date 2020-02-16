def main():
    A,K = map(int,input().split())
    for i in range(10**9):
        if A > 2*10**12:
            print(i)
            break
        else:
            A += 1+K*A

if __name__ == '__main__':
    main()