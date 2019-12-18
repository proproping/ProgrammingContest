import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
print(A*B-A-B+1)
"""

# B
"""
N = int(input())
tmp = []
for i in range(N+1):
    if i%2 != 0:
        tmp.append(i)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
ans = []
for j in range(len(tmp)):
    ans.append(make_divisors(tmp[j]))
count = 0
for k in range(len(ans)):
    if len(ans[k]) == 8:
        count += 1
print(count)
"""

# C
"""
S = input()
K = int(input())
if S[0]*len(S) == S and S[0] == "1":
    print("1")
else:
    ans = 0
    ind = 0
    for i in range(len(S)):
        if S[i] != "1":
            ans = S[i]
            ind = i+1
            break
    if ind > K:
        print("1")
    else:
        print(ans)
"""

# D


# E


# F
