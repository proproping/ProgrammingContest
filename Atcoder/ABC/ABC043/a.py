def main():
    N = int(input())
    if N == 1:
        print(1)
    elif N%2 != 0:
        print((1+N)*(N//2)+(N-N//2))
    else:
        print((1+N)*(N//2))

if __name__ == '__main__':
    main()