import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
print(str(B)+" "+str(A))
"""

# B
"""
N = int(input())
hh = N//3600
mm = (N%3600)//60
ss = (N%3600)%60
print(str(hh).zfill(2)+":"+str(mm).zfill(2)+":"+str(ss).zfill(2))
"""

# C
"""
N = int(input())
tmp = 2025 - N
ans = []
for i in range(1,10):
    if tmp%i == 0 and tmp//i < 10:
        ans.append([i,tmp//i])
for i in range(len(ans)):
    print(*ans[i],sep=" x ")
"""

# D


# E


# F
