import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
inputs = [input() for i in range(2)]
a = int(inputs[0])
s = str(inputs[1])
if a >= 3200:
    print(s)
else:
    print("red")
"""

# B
"""
import numpy as np
n = int(input())
a = np.array(list(map(int,input().split())))
one = np.repeat(1,n)
rec = one/a
recsum = sum(rec)
ans = 1/recsum
print(ans)
"""

# C
"""
N = int(input())
n = list(map(int,input().split()))
for i in range(N-1):
    tmp = []
    tmp.append(n.pop(n.index(min(n))))
    tmp.append(n.pop(n.index(min(n))))
    n.append(sum(tmp)/2)
print(sum(n))
"""

# D


# E


# F
