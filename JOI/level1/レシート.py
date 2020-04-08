def main():
    SUM = int(input())
    book = [int(input()) for _ in range(9)]
    print(SUM - sum(book))

if __name__ == '__main__':
    main()