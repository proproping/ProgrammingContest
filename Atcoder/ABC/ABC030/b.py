def main():
    n,m = map(int,input().split())
    n = n%12
    long = m*(360/60)
    short = n*(360/12)+m*(360/12/60)
    print(min([abs(long-short),360-abs(long-short)]))

if __name__ == '__main__':
    main()