def main():
    import fractions
    A,B,C,D = map(int,input().split())
    def lcm(x,y):
        return (x*y)//fractions.gcd(x,y)
    def cal(n,x,y):
        return n-(n//x + n//y - n//lcm(x,y))
    print(cal(B,C,D)-cal(A-1,C,D))

if __name__ == '__main__':
    main()