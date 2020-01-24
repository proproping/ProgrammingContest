import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from operator import itemgetter
    N = int(input())
    q = []
    ans = 0
    for i in range(N):
        x,l = map(int,input().split())
        q.append([x-l,x+l])
    q = sorted(q,key = itemgetter(1))
    last = -10**18
    for i in range(N):
        tmp = q[i]
        if tmp[0] >= last:
            ans += 1
            last = tmp[1]
    print(ans)

if __name__ == '__main__':
    main()