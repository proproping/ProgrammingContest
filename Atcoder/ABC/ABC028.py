import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
if N == 100:
    print("Perfect")
elif 99 >= N >= 90:
    print("Great")
elif 89 >= N >= 60:
    print("Good")
else:
    print("Bad")
"""

# B
"""
S = list(input())
tmp = [0]*6
for i in range(len(S)):
    if S[i] == "A":
        tmp[0] += 1
    elif S[i] == "B":
        tmp[1] += 1
    elif S[i] == "C":
        tmp[2] += 1
    elif S[i] == "D":
        tmp[3] += 1
    elif S[i] == "E":
        tmp[4] += 1
    else:
        tmp[5] += 1
print(" ".join(list(map(str,tmp))))
"""

# C
"""
import itertools
num = list(map(int,input().split()))
ans = []
tmp = list(map(list,itertools.combinations(range(5),3)))
for i in range(len(tmp)):
    ans.append(num[tmp[i][0]]+num[tmp[i][1]]+num[tmp[i][2]])
print(sorted(ans)[-3])
"""

# D


# E


# F
