import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from collections import Counter
    N = int(input())
    S = list(input())
    c = Counter(S[1:])
    ans = 0+c["E"]
    now = S[0]
    e = c["E"]
    w = 0
    for i in range(1,N):
        if now == "W":
            w += 1
        now = S[i]
        if now == "E":
            e -= 1
        if w+e < ans:
            ans = w+e
    print(ans)

if __name__ == '__main__':
    main()