def main():
    N = int(input())
    a = [int(input()) for i in range(N)]
    count = 0
    tmp = 1
    flag = 0
    for i in range(len(a)):
        if tmp == 2:
            flag = 1
            break
        else:
            tmp = a[tmp-1]
        count += 1
    if flag == 1:
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    main()