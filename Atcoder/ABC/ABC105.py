import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N,K = map(int,input().split())
print("0") if N%K == 0 else print("1")
"""

# B
"""
N = int(input())
c = list(range(0,int(N/4)+1))
d = list(range(0,int(N/7)+1))
ans = "No"
for i in range(len(c)):
    for j in range(len(d)):
        if N - (4*i + 7*j) == 0:
            ans = "Yes"
            break
print(ans)
"""

# C


# D


# E


# F
