def main():
    x,y = map(int,input().split())
    k = int(input())
    n = x+y
    if y >= k:
        print(x+k)
    else:
        print(n-(k-y))

if __name__ == '__main__':
    main()