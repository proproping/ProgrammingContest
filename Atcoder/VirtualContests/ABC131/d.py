import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from operator import itemgetter
    from collections import deque
    N = int(input())
    AB = [list(map(int,input().split())) for _ in range(N)]
    AB = deque(sorted(AB,key = itemgetter(1)))
    ans = "Yes"
    time = 0
    while len(AB) != 0:
        tmp = AB.popleft()
        time += tmp[0]
        if time > tmp[1]:
            ans = "No"
            break
    print(ans)

if __name__ == '__main__':
    main()