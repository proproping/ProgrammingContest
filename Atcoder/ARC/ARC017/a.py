import math

def isPrime(n):
    i = 2
    while True:
        if i**2 > n:
            break
        if n%i == 0:
            return False
        i += 1
    return n != 1


def main():
    N = int(input())
    if isPrime(N):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()