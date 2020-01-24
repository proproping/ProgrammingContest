import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import collections
    S = input()
    c = collections.Counter(S)
    if len(c.values()) == 2:
        print(min(c.values())*2)
    else:
        print(0)

if __name__ == '__main__':
    main()