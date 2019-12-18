import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b = map(int, input().split())
if (a+b)%2 != 0:
    print("IMPOSSIBLE")
else:
    print(int((a+b)/2))
"""

# B
"""
N = int(input())
p = list(map(int,input().split()))
count = 0

for i in range(N):
    if (i+1) != p[i]:
        count += 1

if count <= 2:
    print("YES")
else:
    print("NO")
"""

# C
"""
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
for i in range(N):
    cankill = B[i]
    ans += min([A[i],B[i]])
    if B[i] - A[i] > 0:
        additional = min([B[i] - A[i],A[i+1]])
        ans += additional
        A[i+1] += - additional
print(ans)
"""

# D


# E


# F
