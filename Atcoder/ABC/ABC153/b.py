def main():
    H,N = map(int,input().split())
    A = sorted(list(map(int,input().split())),reverse=True)
    if H <= sum(A[:N]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()