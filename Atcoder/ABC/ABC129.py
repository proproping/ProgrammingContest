import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
P,Q,R = map(int,input().split())
print(P+Q+R-max(P,Q,R))
"""

# B
"""
N = int(input())
W = list(map(int,input().split()))
test = list()
for i in range(N-1):
    test.append(abs(sum(W[0:i+1])-sum(W[i+1:])))
print(min(test))
"""

# C
N,M = map(int,input().split())
a = [int(input()) for _ in range(M)]
st = range(N+1)
for i in range(M):
    st.remove(a[i])
def dfs(now):
    if now == N:
        return True
    if 

# D


# E


# F
