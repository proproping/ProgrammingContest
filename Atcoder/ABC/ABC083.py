import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C,D = map(int,input().split())
if (A+B) - (C+D) == 0:
    print("Balanced")
elif (A+B) - (C+D) > 0:
    print("Left")
else:
    print("Right")
"""

# B
"""
N,A,B = map(int,input().split())
tmp = []
for i in range(1,N+1):
    if A <= sum(list(map(int,list(str(i))))) <= B:
        tmp.append(i)
print(sum(tmp))
"""

# C
"""
X,Y = map(int,input().split())
count = 0
while X <= Y:
    X *= 2
    count += 1
print(count)
"""

# D


# E


# F
