def main():
    from itertools import permutations
    N = int(input())
    P = "".join(list(map(str,input().split())))
    Q = "".join(list(map(str,input().split())))
    ls = permutations(list(range(1,N+1)))
    ans = []
    for i in list(ls):
        ans.append("".join(list(map(str,i))))
    ans = sorted(ans)
    a,b = 0,0
    for i in range(len(ans)):
        if ans[i] == P:
            a = i+1
        if ans[i] == Q:
            b = i+1
    print(abs(int(a)-int(b)))

if __name__ == '__main__':
    main()