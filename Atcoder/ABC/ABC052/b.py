import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    S = input()
    tmp = 0
    ans = 0
    for i in range(N):
        if S[i] == "I":
            tmp += 1
        else:
            tmp += -1
        ans = max([ans,tmp])
    print(ans)

if __name__ == '__main__':
    main()