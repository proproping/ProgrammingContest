import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    S = list(input())
    tmp = [0]*6
    for i in range(len(S)):
        if S[i] == "A":
            tmp[0] += 1
        elif S[i] == "B":
            tmp[1] += 1
        elif S[i] == "C":
            tmp[2] += 1
        elif S[i] == "D":
            tmp[3] += 1
        elif S[i] == "E":
            tmp[4] += 1
        else:
            tmp[5] += 1
    print(" ".join(list(map(str,tmp))))

if __name__ == '__main__':
    main()