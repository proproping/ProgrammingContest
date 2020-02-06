def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = list(input())
        Flags = {"L":False,"R":False,"U":False,"D":False}
        Starts = {"L":0,"R":0,"U":0,"D":0}
        start = 0
        end = 0
        for j in range(n):
            Flags[s[j]] = True
            


if __name__ == '__main__':
    main()