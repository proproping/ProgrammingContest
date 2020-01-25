def main():
    N,K = map(int,input().split())
    l = sorted(list(map(int,input().split())),reverse = 1)
    print(sum(l[:K]))

if __name__ == '__main__':
    main()