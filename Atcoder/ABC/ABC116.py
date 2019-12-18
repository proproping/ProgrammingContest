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
import numpy as np
N = int(input())
h = np.array(list(map(int,input().split())))
count = 0
h -= min(h)
count += min(h)
tmp = "".join([str(n) for n in h])
print(tmp)
"""
# D


# E


# F
