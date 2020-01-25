def main():
    N = int(input())
    n = list(map(int,input().split()))
    for i in range(N-1):
        tmp = []
        tmp.append(n.pop(n.index(min(n))))
        tmp.append(n.pop(n.index(min(n))))
        n.append(sum(tmp)/2)
    print(sum(n))

if __name__ == '__main__':
    main()