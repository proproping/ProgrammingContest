import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    X = int(input())
    ans = 0
    def isPrime(n):
        i = 2
        while i**2 <= n:
            if n%i == 0:
                return False
            i += 1
        return n != 1
    while ans == 0:
        if isPrime(X):
            ans = X
        else:
            X += 1
    print(ans)

if __name__ == '__main__':
    main()