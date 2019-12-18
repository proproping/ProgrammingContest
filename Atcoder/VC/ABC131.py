import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = input()+"t"
ans = "Good"
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        ans = "Bad"
        break
print(ans)
"""

# B
"""
N,L = map(int,input().split())
t = [L+i-1 for i in range(1,N+1)]
abst = list(map(abs,t))
minind = abst.index(min(abst))
print(sum(t)-t[minind])
"""

# C
"""
import math
import fractions
A,B,C,D = map(int,input().split())
def lcm(a,b):
    return (a*b)//fractions.gcd(a,b)
def solve(n,a,b):
    return n - (n//a + n//b - n//lcm(a,b))
print(solve(B,C,D)-solve(A-1,C,D))
"""

# D
"""
from operator import itemgetter
from collections import deque
N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
AB = deque(sorted(AB,key = itemgetter(1)))
ans = "Yes"
time = 0
while len(AB) != 0:
    tmp = AB.popleft()
    time += tmp[0]
    if time > tmp[1]:
        ans = "No"
        break
print(ans)
"""

# E
"""
N,K = map(int,input().split())
if K > (N-1)*(N-2)//2:
    print(-1)
M = (N-1) + ((N-1)*(N-2)//2-K)
tree = [[1,i] for i in range(2,N+1)]
for i in range(2,(M-(N-1)//2-K)+3):
    tree.append([i,i+1])
print(M)
for i in range(len(tree)):
    print(*tree[i],sep = " ")
"""

# F
