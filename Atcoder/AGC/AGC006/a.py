def main():
    N = int(input())
    s = input()
    t = input()
    if s == t:
        print(N)
    else:
        count = 1
        for i in range(1,N):
            tmp = s+t[-i:]
            if s == tmp[:N] and t == tmp[-N:]:
                break
            count += 1
        print(N+count)
if __name__ == '__main__':
    main()