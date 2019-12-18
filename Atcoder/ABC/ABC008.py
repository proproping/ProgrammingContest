import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S,T = map(int,input().split())
print(T-S+1)
"""

# B
"""
N = int(input())
S = [input() for i in range(N)]
tmp1 = list(set(S))
dic = {}
for i in range(len(tmp1)):
    dic.setdefault(tmp1[i],i)
tmp2 = [0]*len(tmp1)
for i in S:
    tmp2[dic[i]] += 1
print(tmp1[tmp2.index(max(tmp2))])
"""

# C


# D


# E


# F
