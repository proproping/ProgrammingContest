def main():
    N = list(str(input()))
    n = int("".join(N))
    sum_N = sum(list(map(int,N)))
    if n%10 == 0 and sum_N == 1:
        print(10)
    else:
        print(sum_N)


if __name__ == '__main__':
    main()