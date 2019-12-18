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
a,b,x = map(int,input().split())
cap = b*a**2
tmp = cap
ans = 90

while tmp > x:

"""

# E


# F
