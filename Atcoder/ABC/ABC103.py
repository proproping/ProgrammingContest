import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A = list(map(int,input().split()))
print(max(A)-min(A))
"""

# B
"""
S = list(input())
T = list(input())
ans = "No"
for i in range(len(S)):
    tmp = S.pop(-1)
    S.insert(0,tmp)
    if S == T:
        ans = "Yes"
        break
print(ans)
"""

# C
"""
N = int(input())
a = list(map(int,input().split()))
print(sum(a)-N)
"""

# D


# E


# F
