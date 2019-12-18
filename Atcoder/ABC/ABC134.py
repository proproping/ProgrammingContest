import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
r = int(input())
print(3*r**2)
"""

# B
"""
N,D = map(int, input().split())
check = (N%(1+2*D))
ans = (N//(1+2*D))
if check == 0:
       print(ans)
else:
       print(ans+1)
"""

# C
"""
N = int(input())
A = [int(input()) for i in range(N)]
maxind = A.index(max(A))
maxa = max(A)
A = sorted(A)
ans = [maxa]*maxind
ans.append(A[-2])
[ans.append(i) for i in [maxa]*(N-maxind-1)]
print(*ans,sep="\n")
"""

# D


# E


# F
