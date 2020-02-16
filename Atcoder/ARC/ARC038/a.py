def main():
    N = int(input())
    A = sorted(list(map(int,input().split())),reverse=True)
    ls = [A[i] for i in range(N) if i%2 == 0]
    print(sum(ls))

if __name__ == '__main__':
    main()