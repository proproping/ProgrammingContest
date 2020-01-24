import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N,K = map(int,input().split())
    dice = list(range(1,N+1))
    count = []
    for i in dice:
        tmp = i
        t = 0
        while tmp < K:
            tmp *= 2
            t += 1
        count.append(t)
    ans = []
    for i in range(len(count)):
        ans.append(1/N*(1/2)**count[i])
    print(sum(ans))

if __name__ == '__main__':
    main()