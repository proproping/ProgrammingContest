import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
X,Y = map(int,input().split())
ans = 0
if X == 3:
    ans += 100000
if X == 2:
    ans += 200000
if X == 1:
    ans += 300000
if Y == 3:
    ans += 100000
if Y == 2:
    ans += 200000
if Y == 1:
    ans += 300000
if X == 1 and Y == 1:
    ans += 400000
print(ans)
"""

# B
# N = int(input())
# A = list(map(int,input().split()))
# mid = sum(A)/2
# length = 0
# i = 0
# while True:
#     if length >= mid:
#         length = min(abs(length-mid),abs(length-mid-A[i-1]))+mid
#         break
#     length += A[i]
#     i += 1
# print(int(length-(sum(A)-length)))
# C


# D


# E


# F
