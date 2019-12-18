import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
s = list(input())
if (s[0] == s[1]) or (s[1] == s[2]) or (s[2] == s[3]):
    print("Bad")
else:
    print("Good")
"""

# B
"""
import numpy as np
N,L = map(int,input().split())
apple = np.array(range(N)) + 1
taste = apple + L - 1
taste_applepie = sum(taste)
if L <= 0 and abs(N) > abs(L):
    print(taste_applepie)
elif L > 0:
    print(taste_applepie - L)
else:
    print(taste_applepie - (N+L-1))
"""

# C
"""
import fractions
A,B,C,D = map(int,input().split())
def lcm(x,y):
    return (x*y)//fractions.gcd(x,y)
def cal(n,x,y):
    return n-(n//x + n//y - n//lcm(x,y))
print(cal(B,C,D)-cal(A-1,C,D))
"""

# D


# E


# F
