def main():
    import math
    from fractions import gcd
    def lll(a,b):
        return (a*b)//gcd(a,b)
    N,M = map(int,input().split())
    a = list(set(map(int,input().split())))
    lcm = a[0]/2
    for i in range(1,len(a)):
        lcm = lll(lcm,a[i]/2)
    ans = int(abs((M//lcm//2) - (M//lcm)))
    print(ans)

if __name__ == '__main__':
    main()