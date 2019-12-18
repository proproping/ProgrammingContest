import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = list(input())
if sorted(S) == ["a","b","c"]:
    print("Yes")
else:
    print("No")
"""

# B
"""
A,B,K = map(int,input().split())
if A == B:
    print(A)
if K > B - A:
    K = B - A
tmp1 = list(range(A,A+K))
tmp2 = list(range(B-K+1,B+1))
ans = sorted(list(set(tmp1 + tmp2)))
for i in ans:
    print(i)
"""

# C
"""
ls = sorted(list(map(int,input().split())))
x = ls[2]*2 - ls[0] - ls[1]
if x%2 == 1:
    x += 3
print(x//2)
"""
# D


# E


# F
