def main():
    N = int(input())
    K = int(input())
    tmp = 1
    for i in range(N):
        tmp = min([tmp*2,tmp+K])
    print(tmp)

if __name__ == '__main__':
    main()