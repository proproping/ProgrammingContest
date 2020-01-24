import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    s = list(input())
    tmp = []
    for i in range(len(s)):
        if s[i] == "0":
            tmp.append("0")
        elif s[i] == "1":
            tmp.append("1")
        elif s[i] == "B" and tmp != []:
            tmp.pop(len(tmp)-1)
    print("".join(tmp))

if __name__ == '__main__':
    main()