def main():
    l = sorted(list(map(int,input().split())))
    print(l[2]) if l[0] == l[1] else print(l[0])

if __name__ == '__main__':
    main()