def main():
    N = int(input())
    r = str(input())
    dic = dict(zip(list("ABCDF"),list(range(4,-1,-1))))
    gp = 0
    for i in r:
        gp += dic[i]
    print(gp/N)

if __name__ == '__main__':
    main()