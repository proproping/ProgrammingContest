def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    u = sum(b)
    for i in range(1,n):
        if a[i] - a[i-1] == 1:
            u = u + c[a[i]-2]
    print(u)

if __name__ == '__main__':
    main()