import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
r,g,b = map(int,input().split())
if (r*100+g*10+b)%4 == 0:
    print("YES")
else:
    print("NO")
"""

# B
"""
N = int(input())
a = list(map(int,input().split()))
print(max(a)-min(a))
"""

# C
"""
N = int(input())
a = list(map(int,input().split()))
col = [0]*8
wild = 0
for i in a:
    if i//400 <= 7:
        col[i//400] = 1
    else:
        wild += 1
minimum = max(1,sum(col))
maximum = sum(col)+wild
print(minimum,maximum)
"""

# D


# E


# F
