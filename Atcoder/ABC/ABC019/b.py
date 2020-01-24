import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    s = list(input())
    ans = []
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            ans.append(str(s[i-1])+str(count))
            count = 1
    ans.append(str(s[-1])+str(count))
    print("".join(ans))

if __name__ == '__main__':
    main()