import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
if A*B%2 == 0:
    print("No")
else:
    print("Yes")
"""

# B
"""
N = int(input())
W = [input() for i in range(N)]
ans = "Yes"
if sorted(set(W)) != sorted(W):
    ans = "No"
else:
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            ans = "No"
            break
print(ans)
"""

# C


# D


# E


# F
