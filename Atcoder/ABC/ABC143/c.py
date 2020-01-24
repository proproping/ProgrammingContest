import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    S = input()
    tmp = 0
    ans = 0
    if S == S[0]*N:
        print(1)
    else:
        for i in range(1,N):
            if S[i] == S[i-1]:
                tmp += 1
        ans = N - tmp
        print(ans)

if __name__ == '__main__':
    main()