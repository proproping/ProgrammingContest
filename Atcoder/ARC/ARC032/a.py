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
    n = int(input())
    if isPrime((n+1)*n/2):
        print("WANWAN")
    else:
        print("BOWWOW")

if __name__ == '__main__':
    main()