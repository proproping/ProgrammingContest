import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    ans = 0
    count = 0
    for i in range(len(S)):
        if S[i] in list("ACGT"):
            count += 1
        else:
            count = 0
        ans = max([ans,count])
    print(ans)

if __name__ == '__main__':
    main()