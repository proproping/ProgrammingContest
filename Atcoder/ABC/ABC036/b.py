import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import numpy as np
    N = int(input())
    mat = [list(input()) for i in range(N)]
    mat = np.array(mat)
    ans = np.rot90(mat,k = -1)
    for i in range(N):
        print("".join(ans[i]))

if __name__ == '__main__':
    main()