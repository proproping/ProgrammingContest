def main():
    from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
    N = int(input())
    a = list(map(int,input().split()))
    ave = Decimal(str(sum(a)/N)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    cost = 0
    for i in a:
        cost += (i-ave)**2
    print(cost)

if __name__ == '__main__':
    main()