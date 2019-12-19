import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b,c = map(str,input().split())
print("A"+str.upper(b[0])+"C")
"""

# B
"""
a,b,x = map(int,input().split())
tmp1 = b//x
tmp2 = (a-1)//x
print(tmp1-tmp2)
"""

# C
"""
N,x = map(int,input().split())
a = list(map(int,input().split()))
count = 0
for i in range(N-1):
    if a[i]+a[i+1] >= x:
        tmp = (a[i]+a[i+1]-x)
        a[i+1] -= tmp
        a[i+1] = max(0,a[i+1])
        count += tmp
print(count)
"""


# D


# E


# F
