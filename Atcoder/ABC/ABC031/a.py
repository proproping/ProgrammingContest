def main():
    A,D = map(int,input().split())
    print((min([A,D])+1)*max([A,D]))

if __name__ == '__main__':
    main()