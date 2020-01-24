import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(2,N):
        if S[i-2:i+1] == "ABC":
            count += 1
    print(count)

if __name__ == '__main__':
    main()