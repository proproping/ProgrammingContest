import sys
import os
f = open('input.txt','r')
sys.stdin = f

# A
from itertools import groupby
r = p = 0
for k,g in groupby(input()):
    l = sum([1 for _ in g])
    r += l*(l+1)//2
    if k == ">":
        r -= min(l,p)
    p = l
print(r)