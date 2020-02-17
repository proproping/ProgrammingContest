from operator import itemgetter
def main():
    N,M = map(int,input().split())
    disk = [int(input()) for _ in range(M)]
    dic = dict(zip(range(N+1),range(N+1)))
    now = 0
    for i in range(M):
        dic[now] = dic[disk[i]]
        dic[disk[i]] = 0
        now = disk[i]
    tmp = sorted([[list(dic.keys())[i],list(dic.values())[i]] for i in range(N+1)],key=itemgetter(1))
    for i in range(1,N+1):
        print(tmp[i][0])

if __name__ == '__main__':
    main()