import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
if A < 10 and B < 10:
    print(A*B)
else:
    print("-1")
"""

# B
"""
N = int(input())
ans = "No"
for i in range(9):
    if N/(i+1) in [1,2,3,4,5,6,7,8,9]:
        ans = "Yes"
        break
print(ans)
"""

# C
"""
N = int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
div = make_divisors(N)
tmp = []
if len(div)%2 == 0:
    tmp.append(div[int(len(div)/2)])
    tmp.append(div[int(len(div)/2-1)])
else:
    tmp.append(div[len(div)//2])
    tmp.append(div[len(div)//2])
ans = 0
ans = sum(tmp)-2
print(ans)
"""

# D
"""
import math
a,b,x = map(int,input().split())
def f(t):
    t = math.radians(t)
    if a * math.tan(t) <= b:
        return a**2 * b - a**3 * math.tan(t) / 2
    else:
        return b**2 / math.tan(t) * a / 2
tmax = 90
tmin = 0
while True:
    tmid = tmin + (tmax-tmin) / 2
    if abs(f(tmid)-x) <= 10**(-9):
        break
    if f(tmid) < x:
        tmax = tmid
    else:
        tmin = tmid
print(tmid)
"""
# E


# F
