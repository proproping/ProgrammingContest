import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
from math import ceil
a,b = map(int,input().split())
print(ceil((a+b)/2))
"""

# B
"""
s = input()
t = input()
tmp1 = "".join(sorted(list(s)))
tmp2 = "".join(sorted(list(t),reverse = 1))
if tmp1 < tmp2:
    print("Yes")
else:
    print("No")
"""

# C
"""
from collections import Counter
N = int(input())
a = list(map(int,input().split()))
count = Counter(a)
a = list(set(a))
ans = 0
for i in a:
    if count[i] >= i:
        ans += count[i]-i
    else:
        ans += count[i]
print(ans)
"""
# D


# E


# F
