import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
if N == 1:
    print(float(1))
elif N%2 == 0:
    print(float(1/2))
else:
    print(float((N//2+1)/N))
"""

# B
"""
N,K = map(int,input().split())
h = list(map(int,input().split()))
ans = 0
for i in range(N):
    if h[i] >= K:
        ans += 1
print(ans)
"""

# C
"""
N = int(input())
toko = list(map(int,input().split()))
tmp = [0]*N
for i in range(N):
    tmp[toko[i]-1] = str(i+1)
print(" ".join(tmp))
"""

# D
"""
A,B = map(int,input().split())
divider_A = list()
divider_B = list()
while A%2 != 0 || A%2 != 1:
    append.divider_A()
"""

# E


# F
