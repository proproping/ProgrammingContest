import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a = int(input())
b = int(input())
if a%b == 0:
    print(0)
else:
    print(b-(a%b))
"""

# B
"""
import numpy as np
n,X = map(int,input().split())
a = np.array(list(map(int,input().split())))
binaryX = bin(X)[2:]
binaryX = list(binaryX.zfill(n))
binaryX.reverse()
binaryX = np.array(list(map(int,binaryX)))
ans = sum(list(a*binaryX))
print(ans)
"""

# C
"""
import numpy as np
a = np.array([1,2,3])
b = np.array([2,3,6])
print(a*b)
"""

# D


# E


# F
