import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b,c = map(int, input().split())
if (c-(a-b)) <= 0:
    print(0)
else:
    print(c-(a-b))
"""

# B
"""
n = int(input())
ans = 0
for i in range(1,n+1):
    if len(str(i)) % 2 == 1:
        ans += 1
print(ans)
"""

# C
"""
N = int(input())
H = list(map(int,input().split()))
ans = "Yes"
for i in range(1,N):
    if H[-i] < H[-i-1]:
        if H[-i]+1 == H[-i-1]:
            H[-i-1] += -1
        else:
            ans = "No"
            break
print(ans)
"""

# D
"""
S = input()
d = S[0]
c = 1
runlength = []
for i in range(1,len(S)):
    if d == S[i]:
        c += 1
    else:
        runlength.append([d,c])
        d = S[i]
        c = 1
    if i == len(S)-1:
        runlength.append([d,c])
ans = [0]*len(S)
ind = -1
for rl in runlength:
    if rl[0] == "R":
        ind += rl[1]
        ans[ind] += rl[1] - rl[1]//2
        ans[ind+1] += rl[1]//2
    else:
        ans[ind] += rl[1]//2
        ans[ind+1] += rl[1] - rl[1]//2
        ind += rl[1]
print(*ans)
"""

# E


# F
