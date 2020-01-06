import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
if N == 1:
    print(1)
elif N%2 != 0:
    print((1+N)*(N//2)+(N-N//2))
else:
    print((1+N)*(N//2))
"""

# B
"""
s = list(input())
tmp = []
for i in range(len(s)):
    if s[i] == "0":
        tmp.append("0")
    elif s[i] == "1":
        tmp.append("1")
    elif s[i] == "B" and tmp != []:
        tmp.pop(len(tmp)-1)
print("".join(tmp))
"""

# C
"""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
N = int(input())
a = list(map(int,input().split()))
ave = Decimal(str(sum(a)/N)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
cost = 0
for i in a:
    cost += (i-ave)**2
print(cost)
"""
# D


# E


# F
