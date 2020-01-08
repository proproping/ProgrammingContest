import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b,c = map(int,input().split())
tmp = sorted([a,b,c])
print(tmp[0]+tmp[1])
"""

# B
"""
S = list(input())
if len(S)%2 != 0:
    del S[-1]
else:
    del S[-1]
    del S[-1]
while S[:int(len(S)/2)] != S[int(len(S)/2):]:
    del S[-1]
    del S[-1]
print(len(S))
"""

# C
"""
from collections import deque
n = int(input())
a = list(map(str,input().split()))
b = deque()
for i in range(n):
    if i%2 == 0:
        b.append(a[i])
    else:
        b.appendleft(a[i])
if n%2 == 0:
    print(" ".join(b))
else:
    b.reverse()
    print(" ".join(b))
"""
# D


# E


# F
