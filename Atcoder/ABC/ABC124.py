import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
print(max(A+(A-1),B+(B-1),A+B))
"""

# B
"""
N = int(input())
H = list(map(int,input().split()))
count = 1
for i in range(1,N):
    if max(H[:i]) <= H[i]:
        count += 1
print(count)
"""

# C
"""
import math
S = input()
pt1 = "01"*math.ceil(len(S)/2)
pt2 = "10"*math.ceil(len(S)/2)
if len(pt1) != len(S):
    pt1 = pt1[:-1]
    pt2 = pt2[:-1]
ans = []
tmp1 = 0
tmp2 = 0
for i in range(len(S)):
    if S[i] != pt1[i]:
        tmp1 += 1
    if S[i] != pt2[i]:
        tmp2 += 1
print(min([tmp1,tmp2]))
"""

# D


# E


# F
