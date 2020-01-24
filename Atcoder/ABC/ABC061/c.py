import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from operator import itemgetter
    N,K = map(int,input().split())
    ls = [list(map(int,input().split())) for _ in range(N)]
    ls = sorted(ls,key=itemgetter(0))
    len = 0
    ans = 0
    i = 0
    while True:
        if len >= K:
            break
        ans = ls[i][0]
        len += ls[i][1]
        i += 1
    print(ans)

if __name__ == '__main__':
    main()