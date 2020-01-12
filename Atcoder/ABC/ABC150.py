import sys
import os
f = open('input.txt','r')
sys.stdin = f

#A
"""
K,X = map(int,input().split())
if 500*K >= X:
    print("Yes")
else:
    print("No")
"""
#B
"""
N = int(input())
S = input()
count = 0
for i in range(2,N):
    if S[i-2:i+1] == "ABC":
        count += 1
print(count)
"""
#C
"""
from itertools import permutations
N = int(input())
P = "".join(list(map(str,input().split())))
Q = "".join(list(map(str,input().split())))
ls = permutations(list(range(1,N+1)))
ans = []
for i in list(ls):
    ans.append("".join(list(map(str,i))))
ans = sorted(ans)
a,b = 0,0
for i in range(len(ans)):
    if ans[i] == P:
        a = i+1
    if ans[i] == Q:
        b = i+1
print(abs(int(a)-int(b)))
"""

#D
"""
import math
from fractions import gcd
def lll(a,b):
    return (a*b)//gcd(a,b)
N,M = map(int,input().split())
a = list(set(map(int,input().split())))
lcm = a[0]/2
for i in range(1,len(a)):
    lcm = lll(lcm,a[i]/2)
ans = int(abs((M//lcm//2) - (M//lcm)))
print(ans)
"""
#E

#F