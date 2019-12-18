import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
s = list(input())
a = list()
b = list()
c = list()
a.append(s[0])
for i in range(1,4):
    if s[i] == a[0]:
        a.append(s[i])
    elif len(b) == 0:
        b.append(s[i])
    elif s[i] == b[0]:
        b.append(s[i])
    else:
        c.append(s[i])
if (len(a) == 2) and (len(b) == 2):
    print("Yes")
else:
    print("No")
"""

# B
"""
n = int(input())
p = list(map(int,input().split()))
count = 0
for i in range(n-2):
    if p[i] < p[i+1] < p[i+2] or p[i] > p[i+1] > p[i+2]:
        count += 1
print(count)
"""

# C
"""
N = int(input())
d = sorted(list(map(int,input().split())))
low = d[N//2-1]
high = d[N//2]
print(high-low)
"""

# D


# E


# F
