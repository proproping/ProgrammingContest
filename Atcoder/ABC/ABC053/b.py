import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    s = list(input())
    start = 0
    end = 0
    for i in range(len(s)):
        if s[i] == "A":
            start = i
            break
    for j in range(len(s)):
        if s[-j-1] == "Z":
            end = -j-1
            break
    if end == -1:
        print(len(s[start:]))
    else:
        print(len(s[start:end+1]))

if __name__ == '__main__':
    main()