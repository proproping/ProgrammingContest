import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = [input() for i in range(12)]
    count = 0
    for i in range(12):
        if "r" in S[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()