def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    species = list(set(A))
    dic = {}
    for i in species:
        dic[i] = 0
    for i in A:
        dic[i] += 1
    if K >= len(species):
        print(0)
    else:
        tmp = sorted(dic.values(),reverse=1)
        print(sum(tmp[K:]))

if __name__ == '__main__':
    main()