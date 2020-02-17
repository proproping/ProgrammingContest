def main():
    A,K = map(int,input().split())
    if K != 0:
        tmp = [0]*50
        tmp[0] = A
        for i in range(1,50):
            tmp[i] = tmp[i-1] + tmp[i-1]*K + 1
            if tmp[i] >= 2*10**12:
                print(i)
                break
    else:
        print(2*10**12-A)

if __name__ == '__main__':
    main()