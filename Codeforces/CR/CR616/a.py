def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = list(map(int,list(str(input()))))
        odd = 0
        even = 0
        for i in range(n):
            if s[i]%2 == 0:
                even += 1
            else:
                odd += 1
        if odd == 0 or (even == 0 and odd < 3):
            print(-1)
        else:
            oddFlag = False
            evenFlag = False
            ans = ""
            for i in range(n):
                if s[i]%2 == 0 a:

if __name__ == '__main__':
    main()