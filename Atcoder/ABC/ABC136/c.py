import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = "Yes"
    for i in range(1,N):
        if H[-i] < H[-i-1]:
            if H[-i]+1 == H[-i-1]:
                H[-i-1] += -1
            else:
                ans = "No"
                break
    print(ans)

if __name__ == '__main__':
    main()