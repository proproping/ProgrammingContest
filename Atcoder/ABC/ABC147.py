import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A = list(map(int,input().split()))
if sum(A) >= 22:
    print("bust")
else:
    print("win")
"""
# B
"""
S = input()
if len(S)%2 == 0:
    tmp1 = S[:len(S)//2]
    tmp2 = S[len(S)//2:]
    tmp2 = tmp2[::-1]
    count = 0
    for i in range(len(tmp1)):
        if tmp1[i] != tmp2[i]:
            count += 1
    print(count)
else:
    tmp1 = S[:len(S)//2]
    tmp2 = S[len(S)//2+1:]
    tmp2 = tmp2[::-1]
    count = 0
    for i in range(len(tmp1)):
        if tmp1[i] != tmp2[i]:
            count += 1
    print(count)
"""
# C
"""
N = int(input())
mat = []
zero = []
for i in range(N):
    A = int(input())
    tmp = [list(map(int,input().split())) for _ in range(A)]
    mat.append(tmp)
ans = N
num = list(range(1,N+1))
flag = [[[] for _ in range(2)] for _ in range(N)]
dic = dict(zip(num,flag))
count = 1
for i in mat:
    for j in range(len(i)):
        dic[i[j][0]][0].append(count)
        dic[i[j][0]][1].append(i[j][1])
    count += 1
tmp = list(dic.values())
pres = []
for i in range(len(tmp)):
    if tmp[i][0] == []:
        pres.append(i+1)
for i in range(len(pres)):
    for j in range(len(tmp)):
        for k in range(len(tmp[j][0])):
            if tmp[j][0][k] == pres[i] and tmp[j][1][k] == 0:
                tmp[j][1][k] = 1
                ans += -1
for i in range(len(tmp)):
    if 0 in tmp[i][1] and 1 in tmp[i][1]:
        ans += -1
for i in range(len(tmp)):
    if 1 in tmp[i][1] or tmp[i][1] == []:
        break
    else:
        if i == len(tmp)-1:
            ans += -1
print(ans)
"""
# D
N = int(input())
T = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for j in range(A):
        T[i].append(list(map(int,input().split())))
S = [[-1] for _ in range(N)]
tmp = list(range(2**N-1,-1,-1))
bins = [format(tmp[i],"0b").zfill(N) for i in range(2**N)]
for i in range(2**N):
    for j in range(N):
        if bins[i][j] == 1:
            for k in range(len(T[i])):
                if S[T[i][k][0]-1] != -1 and S[T[i][k][0]-1] != T[i][k][1]:
                    break
                else:
                    S[T[i][k][0]-1] = T[i][k][1]
    


# E


# F
