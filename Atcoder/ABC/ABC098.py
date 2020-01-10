import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
print(max([A+B,A-B,A*B]))
"""

# B
"""
N = int(input())
S = input()
count = 0
for i in range(N):
    tmpcount = 0
    tmp1 = list(set(S[:i]))
    tmp2 = list(set(S[i:]))
    for j in range(len(tmp1)):
        if tmp1[j] in tmp2:
            tmpcount += 1
    if tmpcount >= count:
        count = tmpcount
print(count)
"""

# C
"""
from collections import Counter
N = int(input())
S = list(input())
c = Counter(S[1:])
ans = 0+c["E"]
now = S[0]
e = c["E"]
w = 0
for i in range(1,N):
    if now == "W":
        w += 1
    now = S[i]
    if now == "E":
        e -= 1
    if w+e < ans:
        ans = w+e
print(ans)
"""

# D


# E


# F
