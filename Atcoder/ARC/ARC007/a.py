def main():
    X = str(input())
    s = list(input())
    s = [i for i in s if i != X]
    print(*s,sep="")


if __name__ == '__main__':
    main()