class UnionFind:
    def __init__(self,n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self,x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self,x,y):
        return self.find(x) == self.find(y)

    def size(self,x):
        return -self.root[self.find(x)]

    def member(self,x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_member(self):
        return {r:self.member(r) for r in self.roots()}

    def __str__(self):
        return "\n".join("{}: {}".format(r,self.member(r)) for r in self.roots())

def main():
    N,M,K = map(int,input().split())
    ans = [0]*N
    uf = UnionFind(M+K+2)
    block_uf = UnionFind(M+1)
    friend_uf = UnionFind(K+1)
    for i in range(M):
        a,b = map(int,input().split())
        uf.unite(a,b)
        block_uf.unite(a,b)
    for i in range(K):
        c,d = map(int,input().split())
        uf.unite(c,d)
        friend_uf.unite(c,d)
    for i in range(N):
        ans[i] = uf.size(i) - 1
    print(ans)


if __name__ == '__main__':
    main()