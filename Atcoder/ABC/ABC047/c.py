import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    count = 0
    for i in range(1,len(S)):
        if S[i-1] != S[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()