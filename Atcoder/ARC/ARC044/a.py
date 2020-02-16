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
        print("Prime")
    else:
        if (N != 1) and (N%10 != 5) and (N%10%2 != 0) and (sum(list(map(int,list(str(N)))))%3 != 0):
            print("Prime")
        else:
            print("Not Prime")


if __name__ == '__main__':
    main()