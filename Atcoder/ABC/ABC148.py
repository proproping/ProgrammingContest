import sys
import os
f = open('input.txt','r')
sys.stdin = f

#A
"""
ls = [1,2,3]
ls.remove(int(input()))
ls.remove(int(input()))
print(ls[0])
"""
#B
"""
N = int(input())
S,T = map(str,input().split())
tmp = []
for i in range(N):
    tmp.append(S[i])
    tmp.append(T[i])
print(*tmp,sep="")
"""

#C
"""
import fractions
A,B = map(int,input().split())
def lcm(x,y):
    return (x*y) // fractions.gcd(x,y)
print(lcm(A,B))
"""

#D
"""
N = int(input())
a = list(map(int,input().split()))
check = 1
count = 0
if 1 not in a:
    print(-1)
else:
    for i in range(N):
        if a[i] != check:
            count += 1
        else:
            check += 1
    print(count)
"""
#E
"""
N = int(input())
if N%2 == 1:
    print(0)
else:
    ans = 0
    N //= 2
    while N > 0:
        ans += N // 5
        N //= 5
    print(ans)
"""
#F
"""
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
N,u,v = map(int,input().split())
u -= 1
v -= 1
ed = [[0]*N for _ in range(N)]
for _ in range(N-1):
    A,B = map(int,input().split())
    ed[A-1][B-1] = 1
    ed[B-1][A-1] = 1
csr = csr_matrix(ed)
ans = int(max(shortest_path(csr,indices=v)))
print(ans-1)
"""