import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = input()
if N[0] == N[2]:
    print("Yes")
else:
    print("No")
"""

# B
"""
A,B,C,D = map(int,input().split())
alice = set(list(range(A,B+1)))
bob = set(list(range(C,D+1)))
if list(alice&bob) == []:
    print(0)
else:
    print(len(alice&bob)-1)
"""

# C
"""
from fractions import gcd
N = int(input())
T = list(set([int(input()) for _ in range(N)]))
ans = 1
def lcm(a,b):
    return (a*b)//gcd(a,b)
for i in range(len(T)):
    ans = lcm(ans,T[i])
print(ans)
"""
# D


# E


# F
