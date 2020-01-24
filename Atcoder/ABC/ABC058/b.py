import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    O = input()
    E = input()
    ans = []
    for i in range(len(list(E))):
        ans.append(O[i])
        ans.append(E[i])
    if len(list(O)) != len(list(E)):
        ans.append(O[-1])
    print("".join(ans))

if __name__ == '__main__':
    main()