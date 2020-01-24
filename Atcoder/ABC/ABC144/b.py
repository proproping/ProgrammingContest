import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    ans = "No"
    for i in range(9):
        if N/(i+1) in [1,2,3,4,5,6,7,8,9]:
            ans = "Yes"
            break
    print(ans)

if __name__ == '__main__':
    main()