import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
n,m = map(int,input().split())
print((n-1)*(m-1))
"""

# B
"""
s = input()
print("".join([s[0]]+[str(len(s[1:-1]))]+[s[-1]]))
"""

# C
"""
N = int(input())
a = list(map(int,input().split()))
four = 0
two = 0
flag = False
for i in a:
    if i%4 == 0:
        four += 1
    elif i%2 == 0:
        two += 1
if two > 1:
    N -= two
    N -= 2
    four -= 1
    flag = True
N -= 2*(four-1)+(3-flag)
if N > 0:
    print("No")
else:
    print("Yes")
"""

# D


# E


# F
