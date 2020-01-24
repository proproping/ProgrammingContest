import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from collections import deque
    n = int(input())
    a = list(map(str,input().split()))
    b = deque()
    for i in range(n):
        if i%2 == 0:
            b.append(a[i])
        else:
            b.appendleft(a[i])
    if n%2 == 0:
        print(" ".join(b))
    else:
        b.reverse()
        print(" ".join(b))

if __name__ == '__main__':
    main()