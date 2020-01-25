def main():
    tmp = list(map(int,input().split()))
    K = int(input())
    for i in range(K):
        tmp[tmp.index(max(tmp))] = max(tmp)*2
    print(sum(tmp))

if __name__ == '__main__':
    main()