import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = input()
    T = input()
    ac = ["a","t","c","o","d","e","r","@"]
    ans = "You can win"
    for i in range(len(S)):
        if S[i] != T[i]:
            if S[i] != "@" and T[i] != "@":
                ans = "You will lose"
                break
            elif S[i] not in ac or T[i] not in ac:
                ans = "You will lose"
                break
    print(ans)

if __name__ == '__main__':
    main()