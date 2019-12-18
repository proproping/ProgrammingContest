import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
l = sorted(list(map(int,input().split())))
print(l[2]) if l[0] == l[1] else print(l[0])
"""

# B
"""
N = int(input())
a = list(map(int,input().split()))
if sum(a)%N != 0:
    print(-1)
else:
    count = 0
    pop = int(sum(a)/N)
    for i in range(N-1):
        if sum(a[:i+1]) != pop*(i+1):
            count += 1
    print(count)
"""

# C


# D


# E


# F
