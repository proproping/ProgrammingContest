import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    tmp = list(map(int,input().split()))
    ta = tmp[:2]
    tb = tmp[2:4]
    T = tmp[4]
    V = tmp[5]
    n = int(input())
    xy = [list(map(int,input().split())) for _ in range(n)]
    tl = T*V
    ans = "NO"
    for i in range(n):
        time = ((xy[i][0]-ta[0])**2+(xy[i][1]-ta[1])**2)**(1/2) + ((tb[0]-xy[i][0])**2+(tb[1]-xy[i][1])**2)**(1/2)
        if time <= tl:
            ans = "YES"
            break
    print(ans)

if __name__ == '__main__':
    main()