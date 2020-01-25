def main():
    import math
    import fractions
    A,B,C,D = map(int,input().split())
    def lcm(a,b):
        return (a*b)//fractions.gcd(a,b)
    def solve(n,a,b):
        return n - (n//a + n//b - n//lcm(a,b))
    print(solve(B,C,D)-solve(A-1,C,D))

if __name__ == '__main__':
    main()