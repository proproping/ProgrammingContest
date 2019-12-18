import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
r = int(input())
print(int(r**2))
"""

# B
"""
N = int(input())
S = input()
if N%2 != 0:
    print("No")
else:
    if S[:int(N/2)] == S[int(N/2):]:
        print("Yes")
    else:
        print("No")
"""

# C
"""
import itertools
N = int(input())
xy = [list(map(int,input().split())) for i in range(N)]
tmp = list(itertools.permutations(list(range(N)),N))
length = []
for i in range(len(tmp)):
    tmplen = 0
    for j in range(N-1):
        tmplen += ((xy[tmp[i][j]][0]-xy[tmp[i][j+1]][0])**2+(xy[tmp[i][j]][1]-xy[tmp[i][j+1]][1])**2)**(1/2)
    length.append(tmplen)
print(sum(length)/len(length))
"""

# D
"""
import math
X,Y = map(int,input().split())
def comb(n,k,p):
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    a=math.factorial(n) %p
    b=math.factorial(k) %p
    c=math.factorial(n-k) %p
    return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p
def power_func(a,b,p):
    if b==0: return 1
    if b%2==0:
        d=power_func(a,b//2,p)
        return d*d %p
    if b%2==1:
        return (a*power_func(a,b-1,p ))%p
if (X+Y)%3 != 0:
    print(0)
else:
    n = int((2*Y-X)/3)
    m = int((2*X-Y)/3)
    nm = n+m
    k = min([n,m,nm-n,nm-m])
    print(comb(nm,k,10**9+7))
"""

# E


# F
