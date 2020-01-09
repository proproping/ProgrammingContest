import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
X,Y = map(str,input().split())
if X == Y:
    print("=")
elif X < Y:
    print("<")
else:
    print(">")
"""

# B
"""
X,Y,Z = map(int,input().split())
count = 0
X += -Z
while X >= (Y+Z):
    X += -(Y+Z)
    count += 1
print(count)
"""

# C
"""
N,M = map(int,input().split())
time = M*1900+(N-M)*100
p = (1/2)**M
print(int(time*(1/p)))
"""
# D


# E


# F
