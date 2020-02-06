def main():
    t = int(input())
    for i in range(t):
        s = int(input())
        opeCount = 0
        while s//10 != 0:
            opeCount += (s//10)*10
            s += ((s//10) - (s//10)*10)
        print(s+opeCount)

if __name__ == '__main__':
    main()