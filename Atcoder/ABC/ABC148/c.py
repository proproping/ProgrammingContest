import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    import fractions
    A,B = map(int,input().split())
    def lcm(x,y):
        return (x*y) // fractions.gcd(x,y)
    print(lcm(A,B))

if __name__ == '__main__':
    main()