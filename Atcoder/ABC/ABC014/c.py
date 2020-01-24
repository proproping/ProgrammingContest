import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import numpy as np
    a = np.array([1,2,3])
    b = np.array([2,3,6])
    print(a*b)

if __name__ == '__main__':
    main()