import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
if A+B >= 10:
    print("error")
else:
    print(A+B)
"""

# B
"""
S = input()
if len(list(S)) == len(list(set(list(S)))):
    print("yes")
else:
    print("no")
"""

# C
"""
N = int(input())
s = sorted([int(input()) for _ in range(N)])
if sum(s)%10 != 0:
    print(sum(s))
else:
    for i in range(N):
        if s[i]%10 != 0:
            print(sum(s)-s[i])
            break
        if i == N-1:
            print(0)
"""
# D


# E


# F
