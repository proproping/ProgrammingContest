import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import math
    a,b,x = map(int,input().split())
    def f(t):
        t = math.radians(t)
        if a * math.tan(t) <= b:
            return a**2 * b - a**3 * math.tan(t) / 2
        else:
            return b**2 / math.tan(t) * a / 2
    tmax = 90
    tmin = 0
    while True:
        tmid = tmin + (tmax-tmin) / 2
        if abs(f(tmid)-x) <= 10**(-9):
            break
        if f(tmid) < x:
            tmax = tmid
        else:
            tmin = tmid
    print(tmid)

if __name__ == '__main__':
    main()