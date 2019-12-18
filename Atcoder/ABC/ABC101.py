import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = input()
ans = 0
for i in range(S):
    if S[i] == "+":
        ans += 1
    else:
        ans += -1
print(ans)
"""

# B
"""
N = list(input())
tmp = 0
for i in range(len(N)):
    tmp += int(N[i])
if int("".join(N))%tmp == 0:
    print("Yes")
else:
    print("No")
"""

# C
"""
import math
N,K = map(int,input().split())
A = list(map(int,input().split()))
print(math.ceil((N-1)/(K-1)))
"""

# D


# E


# F
