from operator import itemgetter

def main():
    n = int(input())
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    st = sorted([[s[i],t[i]] for i in range(n)],key=itemgetter(1))
    now = 0
    ans = 0
    for i in range(n):
        if now <= st[i][0]:
            ans += 1
            now = st[i][1]
    print(ans)

if __name__ == '__main__':
    main()

"""
in
5
1 2 4 6 8
3 5 7 9 10

out
3
"""