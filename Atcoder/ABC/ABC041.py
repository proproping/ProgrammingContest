import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
s = input()
i = int(input())
print(s[i-1])
"""

# B
"""
A,B,C = map(int,input().split())
print(A*B*C%(10**9+7))
"""

# C
"""
N = int(input())
a = [[i,int(tmp)] for i, tmp in enumerate(input().split(),1)]
a.sort(key = lambda x:x[1], reverse=True)
for i in range(N):
    print(a[i][0])
"""
# D


# E


# F
