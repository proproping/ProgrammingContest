def main():
    N = int(input())
    a = list(map(int,input().split()))
    col = [0]*8
    wild = 0
    for i in a:
        if i//400 <= 7:
            col[i//400] = 1
        else:
            wild += 1
    minimum = max(1,sum(col))
    maximum = sum(col)+wild
    print(minimum,maximum)

if __name__ == '__main__':
    main()