import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input().strip())
g = defaultdict(list)

for _ in range(n - 1):
    u, v, w = map(int, input().strip().split())
    g[u].append((v, w))
    g[v].append((u, w))

q = deque([1])
vis = [-1] * (n + 1)
vis[1] = 0
farthest_node = 1

while q:
    x = q.popleft()
    for nxt, wt in g[x]:
        if vis[nxt] == -1:
            vis[nxt] = vis[x] + wt
            q.append(nxt)
            if vis[nxt] > vis[farthest_node]:
                farthest_node = nxt

q.append(farthest_node)
vis = [-1] * (n + 1)
vis[farthest_node] = 0
res = 0

while q:
    x = q.popleft()
    for nxt, wt in g[x]:
        if vis[nxt] == -1:
            vis[nxt] = vis[x] + wt
            q.append(nxt)
            if vis[nxt] > res:
                res = vis[nxt]

print(res)
