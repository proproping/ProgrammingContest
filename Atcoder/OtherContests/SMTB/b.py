import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import math
    N = int(input())
    tmp = math.ceil(N/1.08)
    if math.floor(tmp*1.08) == N:
        print(int(tmp))
    else:
        print(":(")

if __name__ == '__main__':
    main()