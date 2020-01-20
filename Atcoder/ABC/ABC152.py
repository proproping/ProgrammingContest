import sys
import os
f = open('input.txt','r')
sys.stdin = f

#A
"""
N,M = map(int,input().split())
if N == M:
    print("Yes")
else:
    print("No")
"""
#B
"""
a,b = map(int,input().split())
tmp = []
tmp.append(str(a)*b)
tmp.append(str(b)*a)
tmp = sorted(tmp)
print(tmp[0])
"""
#C
"""
N = int(input())
P = list(map(int,input().split()))
ans = 0
minx = 10**9
for i in range(N):
    if minx > P[i]:
        ans += 1
        minx = P[i]
print(ans)
"""

#D
"""
N = int(input())
c = [[0]*10 for _ in range(10)]
for k in range(1,N+1):
    tmp = str(k)
    i = int(tmp[0])
    j = int(tmp[-1])
    c[i][j] += 1
ans = 0
for i in range(10):
    for j in range(10):
        ans += c[i][j] * c[j][i]
print(ans)
"""

#E
"""
mod = 10**9+7
import fractions
def lcm(a,b):
    return (a*b)//fractions.gcd(a,b)
N = int(input())
A = list(map(int,input().split()))
lc = 1
for i in range(N):
    lc = lcm(lc,A[i])
ans = 0
for i in range(N):
    ans += lc//A[i]
print(ans%mod)
"""

#F