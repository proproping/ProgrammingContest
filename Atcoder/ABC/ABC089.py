import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
print(N//3)
"""

# B
"""
N = int(input())
S = input().split()
ans = {3:"Three",4:"Four"}
print(ans[len(set(S))])
"""

# C
"""
from itertools import combinations
dic = dict(zip(list("MARCH"),[0]*len("MARCH")))
N = int(input())
for i in range(N):
    tmp = input()[0]
    if tmp in "MARCH":
        dic[tmp] += 1
c = combinations(list("MARCH"),3)
ans = 0
for i in c:
    ans += dic[i[0]]*dic[i[1]]*dic[i[2]]
print(ans)
"""
# D


# E


# F
