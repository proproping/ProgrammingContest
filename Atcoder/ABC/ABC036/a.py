def main():
    A,B = map(int,input().split())
    tmp = 0
    count = 0
    while tmp < B:
        tmp += A
        count += 1
    print(count)

if __name__ == '__main__':
    main()