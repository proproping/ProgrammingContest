import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)

        divisors.sort()
        return divisors
    div = make_divisors(N)
    tmp = []
    if len(div)%2 == 0:
        tmp.append(div[int(len(div)/2)])
        tmp.append(div[int(len(div)/2-1)])
    else:
        tmp.append(div[len(div)//2])
        tmp.append(div[len(div)//2])
    ans = 0
    ans = sum(tmp)-2
    print(ans)

if __name__ == '__main__':
    main()