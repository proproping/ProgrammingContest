import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    ans = 0
    for i in range(S):
        if S[i] == "+":
            ans += 1
        else:
            ans += -1
    print(ans)

if __name__ == '__main__':
    main()