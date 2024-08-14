import sys
sys.setrecursionlimit(10**6) 
input =sys.stdin.readline
N, M = map(int, input().split())
line = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    line[u].append(v)
    line[v].append(u)

visited = [False] * (N + 1)

def dfs(node):
    for neighbor in line[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        count += 1
    dfs(i) 

print(count)
