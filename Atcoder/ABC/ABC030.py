import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C,D = map(int,input().split())
if B/A == D/C:
    print("DRAW")
elif B/A > D/C:
    print("TAKAHASHI")
else:
    print("AOKI")
"""

# B
"""
n,m = map(int,input().split())
n = n%12
long = m*(360/60)
short = n*(360/12)+m*(360/12/60)
print(min([abs(long-short),360-abs(long-short)]))
"""

# C


# D


# E


# F
