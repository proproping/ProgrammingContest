import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
N,u,v = map(int,input().split())
u -= 1
v -= 1
ed = [[0]*N for _ in range(N)]
for _ in range(N-1):
    A,B = map(int,input().split())
    ed[A-1][B-1] = 1
    ed[B-1][A-1] = 1
csr = csr_matrix(ed)
ans = int(max(shortest_path(csr,indices=v)))
print(ans-1)