def main():
    N = int(input())
    toko = list(map(int,input().split()))
    tmp = [0]*N
    for i in range(N):
        tmp[toko[i]-1] = str(i+1)
    print(" ".join(tmp))

if __name__ == '__main__':
    main()