def main():
    A,B,C = map(int,input().split())
    if A == B == C and A%2 == 0 and B%2 == 0 and C%2 == 0:
        print(-1)
    else:
        for i in range(10**8):
            if A%2 != 0 or B%2 != 0 or C%2 != 0:
                break
            else:
                ta,tb,tc = A,B,C
                A = (tb+tc)/2
                B = (ta+tc)/2
                C = (ta+tb)/2
        print(i)

if __name__ == '__main__':
    main()