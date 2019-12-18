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
"""
c = [list(map(int,input().split())) for i in range(3)]
c11 = a1+b1
c12 = a1+b2
c13 = a1+b3
c21 = a2+b1
c22 = a2+b2
c23 = a2+b3
c31 = a3+b1
c32 = a3+b2
c33 = a3+b3
"""

# D


# E


# F
