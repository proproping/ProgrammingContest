import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b = map(str,input().split())
if a == b:
    print("H")
else:
    print("D")
"""

# B
"""
W,a,b = map(int,input().split())
if (b <= a+W and a <= b) or (a <= b+W and b <= a):
    print(0)
elif a+W < b:
    print(b-(a+W))
else:
    print(a-(b+W))
"""

# C
"""
X = int(input())
t = 1
while True:
    if (t*(t+1)/2) >= X:
        break
    else:
        t += 1
print(t)
"""
# D


# E


# F
