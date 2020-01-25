def main():
    N = int(input())
    if N == 1:
        print(float(1))
    elif N%2 == 0:
        print(float(1/2))
    else:
        print(float((N//2+1)/N))

if __name__ == '__main__':
    main()