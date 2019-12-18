import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
tmp1 = N//2
tmp2 = N%2
ans = [2]*tmp1
if tmp2 != 0:
    ans.append(1)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
"""

# B
"""
N = int(input())
a,b = map(int,input().split())
K = int(input())
P = list(map(int,input().split()))
ans = "YES"
for i in range(len(P)):
    if P[i] in [a,b]:
        ans = "NO"
        break
if ans == "YES":
    if sorted(list(set(P))) != sorted(P):
        ans = "NO"
print(ans)
"""

# C


# D


# E


# F
