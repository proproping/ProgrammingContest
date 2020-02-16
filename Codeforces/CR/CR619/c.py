import itertools

def main():
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())
        ls = ["a"]*(n-m) + ["b"]*(m)
        print(ls)
        p = list(itertools.permutations(ls))
        for j in range(len(p)):
            print(p[i])


if __name__ == '__main__':
    main()