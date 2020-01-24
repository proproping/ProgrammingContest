import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    K = int(input())
    if S[0]*len(S) == S and S[0] == "1":
        print("1")
    else:
        ans = 0
        ind = 0
        for i in range(len(S)):
            if S[i] != "1":
                ans = S[i]
                ind = i+1
                break
        if ind > K:
            print("1")
        else:
            print(ans)

if __name__ == '__main__':
    main()