import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    antenna = [int(input()) for i in range(5)]
    k = int(input())
    ans = "Yay!"

    if max(antenna)-min(antenna) > k:
        print(":(")
    else:
        for i in range(len(antenna)):
            for j in range(len(antenna)):
                if abs(antenna[i]-antenna[j]) > k:
                    ans = ":("
        print(ans)

if __name__ == '__main__':
    main()