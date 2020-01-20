import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
if A-(B*2) < 0:
    print(0)
else:
    print(A-(B*2))
"""

# B
"""
import itertools
N = int(input())
d = list(map(int,input().split()))
tmp = list(itertools.combinations(d,2))
ans = 0
for i in range(len(tmp)):
    ans = ans + (tmp[i][0] * tmp[i][1])
print(ans)
"""

# C
"""
N = int(input())
S = input()
tmp = 0
ans = 0
if S == S[0]*N:
    print(1)
else:
    for i in range(1,N):
        if S[i] == S[i-1]:
            tmp += 1
    ans = N - tmp
    print(ans)
"""

# D
"""
import itertools
import bisect
N = int(input())
L = sorted(list(map(int,input().split())))
ans = 0
for i in range(N-2):
    a = L[i]
    for j in range(i+1,N-1):
        b = L[j]
        ind_cmin = j+1
        ind_cmax = bisect.bisect_left(L,a+b)-1
        ans += ind_cmax - ind_cmin + 1
print(ans)
"""
# E


# F
