import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
x = int(input())
print("ABC") if x < 1200 else print("ARC")
"""

# B
"""
s = list(input())
start = 0
end = 0
for i in range(len(s)):
    if s[i] == "A":
        start = i
        break
for j in range(len(s)):
    if s[-j-1] == "Z":
        end = -j-1
        break
if end == -1:
    print(len(s[start:]))
else:
    print(len(s[start:end+1]))
"""

# C
x = int(input())
count = 0
point = 0
while True:
    point += 6
    count += 1
    if point >= x:
        break
    point += 5
    count += 1
    if point >= x:
        break
print(count)


# D


# E


# F
