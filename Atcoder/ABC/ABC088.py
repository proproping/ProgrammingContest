import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
A = int(input())
if N%500 > A:
    print("No")
else:
    print("Yes")
"""

# B
"""
N = int(input())
a = list(map(int,input().split()))
if len(a)%2 != 0:
    a.append(0)
    N += 1
alice = []
bob = []
for i in range(int(N/2)):
    alice.append(a.pop(a.index(max(a))))
    bob.append(a.pop(a.index(max(a))))
print(sum(alice)-sum(bob))
"""

# C

c = [list(map(int,input().split())) for _ in range(3)]


# D


# E


# F
