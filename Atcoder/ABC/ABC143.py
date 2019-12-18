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
N = int(input())
L = map(int,input().split())
tmp = list(itertools.combinations(L,3))
ans = 0
for i in range(len(tmp)):
    if abs(tmp[i][1] - tmp[i][2]) < tmp[i][0]:
        if tmp[i][0] < (tmp[i][1] + tmp[i][2]):
            ans += 1
print(ans)
"""

# E


# F
