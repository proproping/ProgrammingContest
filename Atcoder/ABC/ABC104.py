import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
R = int(input())
if R < 1200:
    print("ABC")
elif R < 2800:
    print("ARC")
else:
    print("AGC")
"""

# B
"""
S = list(input())
ans = "AC"
if S[0] != "A":
    ans = "WA"
else:
    count = 0
    for i in S[2:-1]:
        if i == "C":
            count += 1
    if count != 1:
        ans = "WA"
    else:
        for i in S:
            if i not in ["A","C"] and str.islower(i) != True:
                ans = "WA"
print(ans)
"""

# C


# D


# E


# F
