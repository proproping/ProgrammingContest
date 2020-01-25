def main():
    N = int(input())
    tmp = 2
    while tmp <= N:
        tmp += tmp
    print(int(tmp/2))

if __name__ == '__main__':
    main()