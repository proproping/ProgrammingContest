def main():
    N = int(input())
    a,b = map(int,input().split())
    K = int(input())
    P = list(map(int,input().split()))
    if a in P or b in P:
        print("NO")
    elif sorted(set(P),key = P.index) != P:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    main()