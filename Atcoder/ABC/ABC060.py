import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C = map(str,input().split())
if A[-1] == B[0] and B[-1] == C[0]:
    print("YES")
else:
    print("NO")
"""

# B
"""
A,B,C = map(int,input().split())
tmpA = A
tmp = []
while A%B != C and A%B not in tmp:
    tmp.append(A%B)
    A += tmpA
if A%B == C:
    print("YES")
else:
    print("NO")
"""

# C
"""
N,T = map(int,input().split())
t = list(map(int,input().split()))
count = 0
for i in range(1,N):
    if t[i-1] + T > t[i]:
        count += t[i-1] + T - t[i]
print(N*T-count)
"""

# D


# E


# F
