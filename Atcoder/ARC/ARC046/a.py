def main():
    N = int(input())
    ls = list(map(str,list(range(1,10))))
    ans = []
    for i in range(1,11):
        for j in range(9):
            ans.append(int(ls[j]*i))
    ans.sort()
    print(ans[N-1])

if __name__ == '__main__':
    main()