import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
inputs = [input() for i in range(2)]
day1 = list(inputs[0])
day2 = list(inputs[1])
count = 0
for i in range(3):
    if day1[i] == day2[i]:
        count +=1
print(count)
"""

# B
"""
a,b = map(int,input().split())
plug = 1
tap = 0
while plug < b:
    plug = plug + a - 1
    tap += 1
print(tap)
"""

# C
"""
N = int(input())
H = list(map(int,input().split()))
count = 0
ans = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        count += 1
        if count > ans:
            ans = count
    else:
        count = 0
print(ans)
"""

# D
"""
N = int(input())
if N == 1:
    print(0)
elif N%2 != 0:
    print((1+(N-1))*((N-1)//2))
else:
    print((1+(N-1))*((N-1)//2)+(N-1)//2+1)
"""

# E


# F
