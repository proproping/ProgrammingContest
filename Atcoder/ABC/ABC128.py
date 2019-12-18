import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,P = map(int,input().split())
print((A*3+P)//2)
"""

# B
"""
N = int(input())
tmp = list()
for i in range(N):
    s,p = input().split()
    tmp.append([s,int(p),i+1])
tmp = sorted(tmp, key = lambda x:x[1], reverse = 1)
tmp = sorted(tmp, key = lambda x:x[0])
tmp = [x[2] for x in tmp]
for i in range(N):
    print(tmp[i])
"""

# C


# D


# E


# F
