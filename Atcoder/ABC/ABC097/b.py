def main():
    from math import floor
    X = int(input())
    if X != 1000:
        tmp = []
        for i in range(2,100):
            tmp.append(floor(X**(1/i))**i)
        print(max(tmp))
    else:
        print(1000)

if __name__ == '__main__':
    main()