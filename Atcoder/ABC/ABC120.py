import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C = map(int,input().split())
money = B
utility = 0
if A > B:
    print(utility)
else:
    while (utility < C) and (money-A >= 0):
        utility += 1
        money -= A
    print(utility)
"""

# B
"""
A,B,K = map(int,input().split())
tmp = []
for i in range(100):
    if A%(i+1) == 0:
        if B%(i+1) == 0:
            tmp.append(i+1)
print(tmp[len(tmp)-K])
"""

# C
"""
import collections
S = input()
c = collections.Counter(S)
if len(c.values()) == 2:
    print(min(c.values())*2)
else:
    print(0)
"""

# D


# E


# F
