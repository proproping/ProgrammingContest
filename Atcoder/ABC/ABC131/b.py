import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import numpy as np
    N,L = map(int,input().split())
    apple = np.array(range(N)) + 1
    taste = apple + L - 1
    taste_applepie = sum(taste)
    if L <= 0 and abs(N) > abs(L):
        print(taste_applepie)
    elif L > 0:
        print(taste_applepie - L)
    else:
        print(taste_applepie - (N+L-1))

if __name__ == '__main__':
    main()