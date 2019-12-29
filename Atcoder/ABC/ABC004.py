import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
print(2*N)
"""

# B
"""
import numpy as np
c = [np.array(list(input())) for i in range(4)]
ans = np.rot90(c,k = -2)
for i in ans:
    print("".join(i))
"""

# C
"""
N = int(input())
ls = [
    123456,
    213456,
    231456,
    234156,
    234516,
    234561,
    324561,
    342561,
    345261,
    345621,
    345612,
    435612,
    453612,
    456312,
    456132,
    456123,
    546123,
    564123,
    561423,
    561243,
    561234,
    651234,
    615234,
    612534,
    612354,
    612345,
    162345,
    126345,
    123645,
    123465,
    ]
print(ls[N%30])
"""
# D


# E


# F
