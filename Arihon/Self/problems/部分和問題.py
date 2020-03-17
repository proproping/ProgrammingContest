def dfs(i,v):
    global flag
    if i == n:
        tmp = v
        sum = 0
        for j in range(n):
            sum += tmp[j]*a[j]
        if sum == k:
            flag = True
    else:
        for j in range(2):
            tmp = v
            tmp[i] = j
            dfs(i+1,tmp)


def main():
    global n,a,k,flag
    n = int(input())
    a = list(map(int,input().split()))
    k = int(input())
    flag = False
    v = [0]*n
    dfs(0,v)
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()