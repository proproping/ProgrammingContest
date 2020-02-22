import math

def main():
    n,a,b = map(int,input().split())
    limit = math.floor(n/2)
    if a > limit:
        a = n - a
    if b > limit:
        b = n - b
    table = [0]*limit
    table[0] = n
    for i in range(1,limit):
        table[i] = table[i-1]*(n-i)//(i+1)
    if n%2 != 0:
        ans = sum(table)*2+1
    else:
        ans = sum(table)*2+1-table[-1]
    ans -= (table[a-1] + table[b-1])
    print(ans)


if __name__ == '__main__':
    main()