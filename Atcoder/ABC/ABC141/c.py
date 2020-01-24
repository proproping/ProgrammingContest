import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import numpy as np
    N,K,Q = map(int,input().split())
    A = [int(input()) for x in range(Q)]
    points = [K]*N
    tmp = [1]*N
    for i in range(Q):
        points[A[i]-1] += 1
    points = list(np.array(points) - Q)
    for i in range(len(points)):
        if points[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()