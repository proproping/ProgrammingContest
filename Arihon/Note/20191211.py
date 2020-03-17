
import sys
import os
f = open('input.txt','r')
sys.stdin = f

"""
V,e = map(int,input().split())
E = [list(map(int,input().split())) for _ in range(e)]

G = [[] for _ in range(e)]
for i in E:
    G[i[0]].append(i[1])
    G[i[1]].append(i[0])

color = [0]*V

def dfs(v,c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i],-c):
            return False
    return True

def solve():
    for i in range(V):
        if color[i] == 0:
            if not dfs(i,1):
                print("No")
                return
    print("Yes")
solve()
"""

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


"""
N,M = map(int,input().split())
edge = [list(map(int,input().split())) for _ in range(M)]
ans = 0
for i in range(M):
    tmp = edge.pop(i)
    uf = UnionFind(N)
    for j in range(M-1):
        u,t = edge[j][0]-1,edge[j][1]-1
        uf.union(u,t)
        uf.union(t,u)
    if uf.group_count() != 1:
        ans += 1
    edge.insert(i,tmp)
print(ans)
"""
"""
class UnionFind():
  def __init__(self, x):
    self.x=x
    self.root=[-1]*(N+1)
    self.rnk=[0]*(N+1)
  
  def Find_root(self, x):
    if self.root[x]<0:
      return x
    else:
      self.root[x]=self.Find_root(self.root[x])
      return self.root[x]
    
  def Unite(self, x, y):
    x = self.Find_root(x)
    y = self.Find_root(y)
    if x==y:
      return
    elif self.rnk[x]>self.rnk[y]:
      self.root[x] += self.root[y]
      self.root[y] = x
    else:
      self.root[y] += self.root[x]
      self.root[x] = y
      if self.rnk[x]==self.rnk[y]:
        self.rnk[y]+=1
  
  def isSameGroup(self, x, y):
    return self.Find_root(x)==self.Find_root(y)
  
  def Count(self, x):
    return -self.root[self.Find_root(x)]

N,M = map(int,input().split())
p = list(map(lambda x : int(x)-1,input().split()))
count = 0
uf = UnionFind(N)
for _ in range(M):
    i,j = map(lambda x : int(x)-1,input().split())
    uf.Unite(i,j)
for i in range(N):
    if uf.isSameGroup(p[i],i):
        count += 1
print(count)
"""
