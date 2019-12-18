import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
if A > 8 or B > 8:
    print(":(")
else:
    print("Yay!")
"""

# B
"""
import numpy as np
D,N = map(int,input().split())
tmp = list(range(1,100))
tmp.append(101)
tmp = np.array(tmp)
tmp = tmp*(100**D)
print(tmp[N-1])
"""

# C
"""
N = int(input())
a = list(map(int,input().split()))
tmp = []
for i in range(N):
    if a[i]%2 == 0:
        tmp.append(a[i])
if tmp == []:
    print(0)
else:
    ans = 0
    for i in range(len(tmp)):
        num = tmp[i]
        count = 0
        while num%2 == 0:
            num = num/2
            count += 1
        ans += count
    print(ans)
"""

# D


# E


# F
