import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    N = int(input())
    lr = [list(map(int,input().split())) for i in range(N)]
    for i in range(N):
        atmp = S[:lr[i][0]-1]
        btmp = list(S[lr[i][0]-1:lr[i][1]])
        btmp.reverse()
        btmp = "".join(btmp)
        ctmp = S[lr[i][1]:]
        S = atmp+btmp+ctmp
    print(S)

if __name__ == '__main__':
    main()