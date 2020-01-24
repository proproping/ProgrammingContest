import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    a,b = map(int,input().split())
    K = int(input())
    P = list(map(int,input().split()))
    ans = "YES"
    for i in range(len(P)):
        if P[i] in [a,b]:
            ans = "NO"
            break
    if ans == "YES":
        if sorted(list(set(P))) != sorted(P):
            ans = "NO"
    print(ans)

if __name__ == '__main__':
    main()