import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b = map(int,input().split())
if a*b%2 == 0:
    print("Even")
else:
    print("Odd")
"""

# B
"""
a,b = input().split()
tmp = int(a+b)
if tmp == int(tmp**(1/2))**2:
    print("Yes")
else:
    print("No")
"""

# C
"""
N = int(input())
txy = []
for i in range(N):
    txy.append(list(map(int,input().split())))
ans = "Yes"
t = 0
x = 0
y = 0
for i in range(N):
    deft = txy[i][0] - t
    defx = abs(txy[i][1] - x)
    defy = abs(txy[i][2] - y)
    t = txy[i][0]
    x = txy[i][1]
    y = txy[i][2]
    if (defx + defy) > deft:
        ans = "No"
        break
    elif (deft - defx - defy)%2 != 0:
        ans = "No"
        break
print(ans)
"""

# D


# E


# F
