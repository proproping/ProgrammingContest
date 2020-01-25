def main():
    ls = sorted(list(map(int,input().split())))
    print(sum(ls)-max(ls))

if __name__ == '__main__':
    main()