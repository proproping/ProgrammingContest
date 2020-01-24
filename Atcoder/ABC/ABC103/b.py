import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = list(input())
    T = list(input())
    ans = "No"
    for i in range(len(S)):
        tmp = S.pop(-1)
        S.insert(0,tmp)
        if S == T:
            ans = "Yes"
            break
    print(ans)

if __name__ == '__main__':
    main()