def main():
    C = list(map(int,input().split()))
    V = [1,5,10,50,100,500]
    A = int(input())
    ans = 0
    for i in range(5,-1,-1):
        t = min(A//V[i],C[i])
        A -= t * V[i]
        ans += t
    print(ans)

if __name__ == '__main__':
    main()

"""
in
3 2 1 3 0 2
620

out
6
"""