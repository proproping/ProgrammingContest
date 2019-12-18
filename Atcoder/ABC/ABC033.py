import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = input()
print("SAME") if N[0]*4 == N else print("DIFFERENT")
"""

# B
"""
N = int(input())
cities = [input().split() for i in range(N)]
sumpop = 0
for i in range(N):
    sumpop += int(cities[i][1])
ans = "atcoder"
for j in range(N):
    if int(cities[j][1]) > sumpop/2:
        ans = cities[j][0]
        break
print(ans)
"""

# C


# D


# E


# F
