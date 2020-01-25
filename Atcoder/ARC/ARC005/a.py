import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    from collections import Counter
    N = int(input())
    w = list(map(str,input().split()))
    w[-1] = w[-1][:-1]
    c = Counter(w)
    print(c["TAKAHASHIKUN"]+c["takahashikun"]+c["Takahashikun"])

if __name__ == '__main__':
    main()