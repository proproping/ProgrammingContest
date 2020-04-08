def main():
    a = sorted([int(input()) for _ in range(4)],reverse=True)
    b = sorted([int(input()) for _ in range(2)],reverse=True)
    print(sum(a[:3])+sum(b[:1]))

if __name__ == '__main__':
    main()