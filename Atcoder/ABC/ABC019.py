import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
from statistics import median
a,b,c = map(int,input().split())
print(median([a,b,c]))
"""

# B
"""
s = list(input())
ans = []
count = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        ans.append(str(s[i-1])+str(count))
        count = 1
ans.append(str(s[-1])+str(count))
print("".join(ans))
"""

# C


# D


# E


# F
