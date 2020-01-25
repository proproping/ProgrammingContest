def main():
    n = int(input())
    h = 1
    w = 1
    tmp = []
    while h*w <= n:
        w = n//h
        tmp.append(abs(h-w)+n-h*w)
        h += 1
        w = 1
    print(min(tmp))

if __name__ == '__main__':
    main()