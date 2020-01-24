import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    s = {}
    ans = 0
    for i in range(N):
        a = "".join(sorted(input()))
        if a not in s:
            s.setdefault(a,0)
        else:
            s[a] += 1
            ans += s[a]
    print(ans)

if __name__ == '__main__':
    main()