# メモ化再帰
# def rec(i,j):
#     if dp[i][j] >= 0:
#         return dp[i][j]
#     res = 0
#     if i == n:
#         res = 0
#     elif j < w[i]:
#         res = rec(i+1,j)
#     else:
#         res = max(rec(i+1,j),rec(i+1,j-w[i])+v[i])
#     dp[i][j] = res
#     return res
# def main():
#     global n,w,v,dp
#     n = int(input())
#     w,v = [0]*n,[0]*n
#     for i in range(n):
#         w[i],v[i] = map(int,input().split())
#     W = int(input())
#     dp = [[-1]*(W+1) for _ in range(n+1)]
#     print(rec(0,W))

# 貰うDP
# def main():
#     global n,w,v,dp
#     n,W = map(int,input().split())
#     w,v = [0]*(n),[0]*(n)
#     for i in range(n):
#         w[i],v[i] = map(int,input().split())
#     dp = [[0]*(W+1) for _ in range(n+1)]
#     for i in range(1,n+1):
#         for j in range(1,W+1):
#             if j < w[i-1]:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
#     print(dp[n][W])

# 配るDP
def main():
    global n,w,v,dp
    n,W = map(int,input().split())
    w,v = [0]*n,[0]*n
    for i in range(n):
        w[i],v[i] = map(int,input().split())
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(W+1):
            if j < w[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]]+v[i])
    print(dp[n][W])

if __name__ == '__main__':
    main()

"""
in
4 5
2 3
1 2
3 4
2 2

out
7
"""