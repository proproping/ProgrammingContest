import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    s = sorted([int(input()) for _ in range(N)])
    if sum(s)%10 != 0:
        print(sum(s))
    else:
        for i in range(N):
            if s[i]%10 != 0:
                print(sum(s)-s[i])
                break
            if i == N-1:
                print(0)

if __name__ == '__main__':
    main()