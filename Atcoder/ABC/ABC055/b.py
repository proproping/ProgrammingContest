import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from math import factorial
    N = int(input())
    print(factorial(N)%(10**9+7))

if __name__ == '__main__':
    main()