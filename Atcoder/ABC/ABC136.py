import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b,c = map(int, input().split())
if (c-(a-b)) <= 0:
    print(0)
else:
    print(c-(a-b))
"""

# B
"""
n = int(input())
ans = 0
for i in range(1,n+1):
    if len(str(i)) % 2 == 1:
        ans += 1
print(ans)
"""

# C
"""
N = int(input())
H = list(map(int,input().split()))
ans = "Yes"
for i in range(1,N):
    if H[-i] < H[-i-1]:
        if H[-i]+1 == H[-i-1]:
            H[-i-1] += -1
        else:
            ans = "No"
            break
print(ans)
"""

# D


# E


# F
