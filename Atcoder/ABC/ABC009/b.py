def main():
    N = int(input())
    A = list(set([int(input()) for i in range(N)]))
    A.remove(max(A))
    print(max(A))

if __name__ == '__main__':
    main()