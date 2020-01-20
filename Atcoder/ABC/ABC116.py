import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
AB,BC,CA = map(int,input().split())
print(int(AB*BC/2))
"""

# B
"""
s = int(input())
def fn(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1
tmp = [s]
flag = 1
count = 1
while flag == 1:
    count += 1
    s = fn(s)
    tmp.append(s)
    if s in tmp[:-1]:
        break
print(count)
"""

# C
"""
from collections import deque
import numpy as np
N = int(input())
h = np.array(list(map(int,input().split())))
count = 0
tmp = deque()
tmp.append(h)
while True:
    st,en = -1,-1
    if len(tmp) == 0:
        break
    count += min(tmp[0])
    tmp[0] -= min(tmp[0])
    if list(tmp[0]) == [0]*len(tmp[0]):
        tmp.popleft()
        continue
    for i in range(len(tmp[0])):
        if st == -1 and tmp[0][i] != 0:
            st = i
        if st != -1 and tmp[0][i] == 0:
            en = i
        if st != -1 and i == len(tmp[0])-1 and tmp[0][i] != 0:
            en = i+1
        if st != -1 and en != -1:
            tmp.append(tmp[0][st:en])
            st,en = -1,-1
    tmp.popleft()
print(count)
"""
# D


# E


# F
