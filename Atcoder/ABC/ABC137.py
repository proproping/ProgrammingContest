import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b = map(int, input().split())
print(max(a+b,a*b,a-b))
"""

# B
"""
import numpy as np
k,x = map(int,input().split())
ans = np.arange((x-k+1),(x+k))
for i in range(len(ans)):
    print(ans[i], end = " ")
"""

# C
"""
N = int(input())
s = {}
ans = 0
for i in range(N):
    a = "".join(sorted(input()))
    if a not in s:
        s.setdefault(a,0)
    else:
        s[a] += 1
        ans += s[a]
print(ans)
"""

# D


# E


# F
