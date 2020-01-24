import sys
import os
f = open('input.txt','r')
sys.stdin = f

def main():
    N = int(input())
    tmp = []
    for i in range(N+1):
        if i%2 != 0:
            tmp.append(i)
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)

        # divisors.sort()
        return divisors
    ans = []
    for j in range(len(tmp)):
        ans.append(make_divisors(tmp[j]))
    count = 0
    for k in range(len(ans)):
        if len(ans[k]) == 8:
            count += 1
    print(count)

if __name__ == '__main__':
    main()