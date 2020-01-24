import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()+"t"
    ans = "Good"
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans = "Bad"
            break
    print(ans)

if __name__ == '__main__':
    main()